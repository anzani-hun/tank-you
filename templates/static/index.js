console.log('Index teszt szöveg');

const refuelsEl = document.querySelector('#refuels')


// Tankolási adatok
fetch('/api/refuels/')
.then(res => res.json())
.then(data => {
    data.forEach(refuel => {
        element = document.createElement('div')
        element.innerText = refuel.distance
        refuelsEl.appendChild(element)
    });
})



fetch('api/consumption')
.then(res => res.json())
.then(data => {
    let cons = document.getElementById('consumption')
    cons.innerText = data.consumption
})