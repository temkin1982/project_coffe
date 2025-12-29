import { useEffect, useState } from "react";
import CoffeeItem from "../components/CoffeeItem";

const coffeeListDemo = [
    { coffeeId: 1, name: "coffee 1", description: 'תיאור של הקפה', price: 8.99, image: "/FlatWhite.jpeg" },
    { coffeeId: 2, name: "תפוז עצבני 2", description: 'תיאור של הקפה', price: 8.99, image: "/Americano.jpeg" },
    { coffeeId: 3, name: "אגס ביישן 3", description: 'תיאור של הקפה', price: 8.99, image: "/Cappuccino.jpeg" },
    { coffeeId: 4, name: "coffee 4", description: 'תיאור של הקפה', price: 8.99, image: "/Espresso.jpeg" },
    { coffeeId: 5, name: "הדהוד האגוז 5", description: 'תיאור של הקפה', price: 8.99, image: "/Latte.jpeg" },
    { coffeeId: 6, name: "נגיעות של משהו 6", description: 'תיאור של הקפה', price: 8.99, image: "/coffee.jpg" },
]
function CoffeeList() {
    const [coffeeList, setCoffeeList] = useState([])

    const loadCoffee = () => {
        setCoffeeList(coffeeListDemo)
    }
    useEffect(() => {
        loadCoffee();
    }, [])

    return (
        <div>
            {
                coffeeList.map((c) => <CoffeeItem key={c.coffeeId} coffee={c}/>)
            }
        </div>
    )
}

export default CoffeeList;