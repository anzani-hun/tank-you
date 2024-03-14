console.log('Index teszt szöveg');

const refuelsEl = document.querySelector('#refuels')

// Tankolási adatok
fetch('/api/refuels/')
.then(res => res.json())
.then(data => {
    data.forEach(refuel => {

        wrapper = document.createElement("div")

        element = document.createElement('h3')
        element.innerText = refuel.distance
        wrapper.appendChild(element)

        petrol = document.createElement('h4')
        petrol.innerText = refuel.petrol_amount_litre + "litre"
        wrapper.appendChild(petrol)

        date = document.createElement('h4')
        d = new Date(refuel.refuel_date)

        const options = { year: 'numeric', month: 'long', day: 'numeric'};
        date.innerText = d.toLocaleDateString('hu-HU', options);
        //date.innerText = d
        wrapper.appendChild(date)

        refuelsEl.appendChild(wrapper)
    });
})



fetch('api/consumption')
.then(res => res.json())
.then(data => {
    let cons = document.getElementById('consumption')
    cons.innerText = data.consumption
})