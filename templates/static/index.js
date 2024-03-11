console.log('Index teszt szöveg');

const refuelsEl = document.querySelector('#refuels')

fetch('/api/refuels/')
.then(res => res.json())
.then(data => {
    data.forEach(refuel => {
        element = document.createElement('div')
        element.innerText = refuel.distance
        refuelsEl.appendChild(element)
    });
})