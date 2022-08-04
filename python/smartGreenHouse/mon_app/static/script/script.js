const gaugeElement1 = document.getElementById("g1");
const gaugeElement2 = document.getElementById("g2");
const gaugeElement3 = document.getElementById("g3");
const gaugeElement4 = document.getElementById("g4");

function setGaugeValue(gauge, value) {
    if (value < 0 || value > 1) {
        return;
    }

    gauge.querySelector(".gauge__fill").style.transform = `rotate(${
    value / 2
  }turn)`;
    gauge.querySelector(".gauge__cover").textContent = `${Math.round(
    value * 100
  )}%`;
}
var value1 = 30
var value2 = 50
var value3 = 70
var value4 = 90

var Pourcentage_value1 = value1 / 100
var Pourcentage_value2 = value2 / 100
var Pourcentage_value3 = value3 / 100
var Pourcentage_value4 = value4 / 100
setGaugeValue(gaugeElement1, Pourcentage_value1);
setGaugeValue(gaugeElement2, Pourcentage_value2);
setGaugeValue(gaugeElement3, Pourcentage_value3);
setGaugeValue(gaugeElement4, Pourcentage_value4);