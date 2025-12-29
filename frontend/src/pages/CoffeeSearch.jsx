import { useState, useRef, useEffect } from "react"
import CoffeeItem from '../components/CoffeeItem'
const coffeeListDemo = [
    { coffeeId: 1, name: "coffee 1", description: 'תיאור של הקפה', price: 8.99, image: "/FlatWhite.jpeg" },
    { coffeeId: 2, name: "תפוז עצבני 2", description: 'תיאור של הקפה', price: 8.99, image: "/Americano.jpeg" },
    { coffeeId: 3, name: "אגס ביישן 3", description: 'תיאור של הקפה', price: 8.99, image: "/Cappuccino.jpeg" },
    { coffeeId: 4, name: "coffee 4", description: 'תיאור של הקפה', price: 8.99, image: "/Espresso.jpeg" },
    { coffeeId: 5, name: "הדהוד האגוז 5", description: 'תיאור של הקפה', price: 8.99, image: "/Latte.jpeg" },
    { coffeeId: 6, name: "נגיעות של משהו 6", description: 'תיאור של הקפה', price: 8.99, image: "/coffee.jpg" },
]
function CoffeeSearch() {
    // כאשר מקבלים רשימה מהשרת
    // עוברים על הרשימה באמצעות map
    // כדי להציג כל איבר
    const [coffeeList, setCoffeeList] = useState([])
    const [text, setText] = useState("")

    useEffect(() => {

        setCoffeeList(coffeeListDemo)
    }, [])
    // מגדיר זיכרון קבוע לטג גם אחרי עדכון
    const txtRef = useRef(null);
    //<button onClick={search}>search</button>
    // b =document.getElementById(....)
    // b.addEventListener('click', search)
    function search() {
        console.log(txtRef.current.value);
        setText(txtRef.current.value)
    }

    function filterCoffee() {
        if (text.length == 0) {
            return coffeeList
        } else {
            return coffeeList.filter((c) => c.name.includes(text))  // .map( (c)=>({...c, name:c.name+" fff"}) )
        }
    }

    // if(!state)return <div>loading</div>
    return (
        <div>

            <div>
                <div>menu</div>
                <div>
                    <h1>title</h1>
                    <h3>sub title</h3>
                </div>
                <div>
                    <h3>Search</h3>
                    <input type="text" ref={txtRef} />
                    <button onClick={search}>search</button>
                </div>
            </div>
            <div>
                <h2>about</h2>
                <p>about text</p>
            </div>
            <div>
                {
                    filterCoffee().map((c) => <CoffeeItem key={c.id} coffee={c} />)
                }
            </div>
            <div>
                <div>menu</div>
            </div>
        </div>
    )

}


export default CoffeeSearch;