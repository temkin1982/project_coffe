import { useState } from "react";

function CreateCoffee() {

    const [coffee, setCoffee] = useState({ name: "", description: "", price: 0, image: "" })

    const onChange = (event) => {

        const value = event.target.value;
        const name = event.target.name;

        setCoffee({ ...coffee, [name]: value })
    }

    const onSubmit = (event) => {
        event.preventDefault();
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <input type="text" required name="name" value={coffee.name} onChange={onChange} placeholder="coffee name" />
            </div>
            <div>
                <textarea required name="description" value={coffee.description} onChange={onChange} placeholder="coffee description"></textarea>
            </div>
            <div>
                <input type="number" required name="price" value={coffee.price} onChange={onChange} placeholder="coffee price" style={{ direction: 'ltr' }} />
            </div>
            <div>
                <input type="file" name="image" onChange={onChange} />
            </div>
            <br />
            <button>Register</button>
        </form>
    )
}

export default CreateCoffee;