"""Views Creation"""
import random
from flask import request, render_template, url_for, redirect

from app import app

from .universe_creation import Player, Universe, Game, Bandit, Police, Trader


class Updater:
    """Updater Class"""
    id_to_game = {}
    id_to_npc = {}


@app.route('/')
def index():
    """Index"""
    Universe.get_instance()
    return render_template("index.html")


@app.route('/config')
def about():
    """About"""
    Universe.get_instance()
    return render_template("configure.html")


@app.route('/game/<int:g_id>')
def game(g_id):
    """Game"""
    game = Updater.id_to_game[g_id]
    if game.player.ship.current_health <= 0:
        return redirect(url_for('gameover'))
    if game.player.karma > 5 and random.randint(0, 3) == 0:
        game.player.currency *= 1.1
    elif game.player.karma < -5 and random.randint(0, 3) == 0:
        game.player.currency *= 0.9
    return render_template('game.html', g_id=g_id, game=game,
                           regions=Universe.regions(), player=game.player)


@app.route('/buywin/<int:g_id>')
def buywin(g_id):
    """Buy Win"""
    game = Updater.id_to_game[g_id]
    if game.player.currency >= 750:
        return redirect(url_for('gamewin'))
    return redirect(url_for('game', g_id=g_id))


@app.route('/gameover')
def gameover():
    """Game Over"""
    return render_template('gameover.html')


@app.route('/gamewin')
def gamewin():
    """Game Win"""
    return render_template('gamewin.html')


@app.route('/game/<int:g_id>/travel/<string:name>/<int:activate>')
def travel(g_id, name, activate):
    """Travel"""
    game = Updater.id_to_game[g_id]
    for region in Universe.regions():
        if region.name == name:
            distance = pow(pow(game.player.region.y_coordinate - region.y_coordinate, 2) +
                           pow(game.player.region.x_coordinate - region.x_coordinate, 2), 0.5)
            cost = distance - (game.player.pilot_points * 3.5) if game.player.pilot_points <= 4\
                else distance / (.25 * game.player.pilot_points)
            cost = round(cost, 2)
            if game.player.ship.current_fuel - cost > 0:
                # chance to encounter
                if game.difficulty in ['easy', 'normal']:
                    chance = random.randint(0, 99)
                    if chance > 50:
                        if chance > 69:
                            # traveler
                            g_id = update_id(game)
                            return redirect(url_for('interupt', g_id=g_id,
                                                    name="Trader", region=name))
                        # other place
                        chance2 = random.randint(1, 2)
                        g_id = update_id(game)
                        if chance2 == 2 and len(game.player.inventory) > 0:
                            return redirect(url_for('interupt', g_id=g_id,
                                                    name="Police", region=name))
                        credit_demand = random.randint(0, player.credits +
                                                       random.randint(0,
                                                                      Bandit.credits / 50))
                        return redirect(url_for('interupt', g_id=g_id, name="Bandit",
                                                region=name, demand=credit_demand))
                else:
                    chance = random.randint(0, 99)
                    if chance > 50 and activate > 0:
                        if chance > 78:
                            # traveler
                            g_id = update_id(game)
                            return redirect(url_for('interupt', g_id=g_id,
                                                    name="Trader", region=name))
                        # other place
                        chance2 = random.randint(1, 2)
                        g_id = update_id(game)
                        if chance2 == 2 and len(game.player.inventory) > 0:
                            return redirect(url_for('interupt', g_id=g_id,
                                                    name="Police", region=name))
                        return redirect(url_for('interupt', g_id=g_id,
                                                name="Bandit", region=name))
                game.player.ship.current_fuel = round(game.player.ship.current_fuel - cost, 2)
                game.player.region = region
                break
    g_id = update_id(game)
    return redirect(url_for('game', g_id=g_id))


@app.route('/fuel/<int:g_id>')
def fuel(g_id):
    """Fuel"""
    game = Updater.id_to_game[g_id]
    if game.player.ship.current_fuel + 50 < game.player.ship.fuel_max:
        if game.player.credits >= 50:
            game.player.credits -= 10
            game.player.ship.current_fuel += 50
    else:
        diff = 1000 - game.player.ship.current_fuel
        if game.player.credits >= .2 * diff:
            game.player.credits -= .2 * diff
            game.player.credits = round(game.player.credits, 2)
            game.player.ship.current_fuel = 1000
    g_id = update_id(game)
    return redirect(url_for('game', g_id=g_id))


@app.route('/heal/<int:g_id>/<float:amt>')
def heal(g_id, amt):
    """Heal"""
    game = Updater.id_to_game[g_id]
    if game.player.credits >= 10:
        if game.player.ship.current_health + amt > 100:
            game.player.ship.current_health = 100
        else:
            game.player.ship.current_health += amt
    g_id = update_id(game)
    return redirect(url_for('game', g_id=g_id))


@app.route('/interupt/<int:g_id>/<string:name>/<string:region>')
def interupt(g_id, name, region):
    """Interrupt"""
    game = Updater.id_to_game[g_id]
    if name == 'Bandit':
        npc = Bandit()
    elif name == 'Trader':
        npc = Trader()
    else:
        npc = Police()
    Updater.id_to_npc = {}
    Updater.id_to_npc[id(npc)] = npc
    return render_template('interupt.html', g_id=g_id, npc_id=id(npc),
                           game=game, name=name, region_name=region,
                           regions=Universe.regions(), player=game.player, npc=npc)


@app.route('/npc/<int:g_id>/<int:npc_id>/<string:region>/<int:action>')
def npc(g_id, npc_id, region, action):
    """NPC"""
    game = Updater.id_to_game[g_id]
    npc = Updater.id_to_npc[npc_id]
    npc.interact(game.player, action)
    if action == 4:
        return redirect(url_for('interupt', g_id=g_id, name="Trader", region=region))
    return redirect(url_for('travel', g_id=g_id, name=region, activate=0))


@app.route('/market/<int:g_id>')
def market(g_id):
    """Market"""
    game = Updater.id_to_game[g_id]
    return render_template('market.html', game=game, g_id=g_id,\
                           player=Updater.id_to_game[g_id].player)


@app.route('/<string:option>/<int:g_id>/buy/<string:item>/<float:amount>')
def buy(option, g_id, item, amount):
    """Buy Method"""
    game = Updater.id_to_game[g_id]
    game.player.region.market.buy(game.player, item)
    g_id = update_id(game)
    amount += 1
    amount -= 1
    game.player.karma += 1
    if option == 'game':
        return redirect(url_for('game', g_id=g_id))
    return redirect(url_for('market', g_id=g_id))


@app.route('/<string:option>/<int:g_id>/sell/<string:item>/<float:amount>')
def sell(option, g_id, item, amount):
    """Sell Method"""
    game = Updater.id_to_game[g_id]
    game.player.region.market.sell(game.player, item)
    g_id = update_id(game)
    amount += 1
    amount -= 1
    game.player.karma += 1
    if option == 'game':
        return redirect(url_for('game', g_id=g_id))
    return redirect(url_for('market', g_id=g_id))


def update_id(game):
    """Update ID"""
    game.update()
    Updater.id_to_game = {}
    g_id = id(game)
    Updater.id_to_game[g_id] = game
    return g_id


@app.route('/config', methods=['POST'])
def to_game():
    """To Game"""
    name = request.form.get('name')
    difficulty = request.form.get('difficulty')
    p_occupation = request.form.get('p_occupation')
    f_occupation = request.form.get('f_occupation')
    m_occupation = request.form.get('m_occupation')
    e_occupation = request.form.get('e_occupation')
    player = Player(name, difficulty, p_occupation, f_occupation, m_occupation, e_occupation)
    g_game = Game(player, difficulty)
    g_game.start_game()
    gid = update_id(g_game)
    return redirect(url_for('game', g_id=gid))
