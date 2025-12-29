import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

function CoffeePage(){
    const[coffee, setCoffee] = useState({coffeeId: 5, name: "הדהוד האגוז 5", description: 'תיאור של הקפה', price: 8.99, image: "/Latte.jpeg"})
    const params = useParams();
    const getCoffee = async()=>{

    }
    useEffect(()=>{
        getCoffee();
    }, [])
  
    return(
        <div>
            <h2>{coffee.name}</h2>
            <p>{coffee.description}</p>
            <img src={coffee.image} alt={coffee.name}/>
            <code>price {coffee.price} </code>
        </div>
    )

}

export default CoffeePage;