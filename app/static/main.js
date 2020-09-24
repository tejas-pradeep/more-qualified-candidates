var diff = ""
var skillPoints = -1;
var rem = -1;
function updatePoints() {
    var radios = document.getElementsByName("difficulty")
    for (var i = 0;i<radios.length;i++) {
        if (radios[i].checked) {
            diff = radios[i].value
        }
    }
    var sp = document.getElementById("skill_points")
    skillPoints = -1;
    if (diff == "easy") {
        skillPoints = 16;
    } else if (diff == "normal") {
        skillPoints = 12;
    } else {
        skillPoints = 8;
    }
    sp.innerHTML = "Skill Points Remaining: " + skillPoints;
    var occupations = document.getElementsByClassName("occupation")
    for (var i = 0;i < occupations.length; i++) {
        occupations[i].value = "0"
        occupations[i].max = ""+skillPoints;
    }
}
function updateAvailablePoints() {
    if (diff == "") {
        alert("please choose a difficulty")
    } else {
        var occupations = document.getElementsByClassName("occupation")
        total = 0
        for (var i = 0;i < occupations.length; i++) {
            total += parseInt(occupations[i].value)
        }
        if (total < 0) {
            updatePoints()
        }
        rem = skillPoints - total;
        document.getElementById("skill_points").innerHTML = "Skill Points Remaining: " + rem;
        for (var i = 0;i < occupations.length; i++) {
            var m = parseInt(occupations[i].value) + rem;
            occupations[i].max = ""+m;

        }
        console.log(total)
    }
}