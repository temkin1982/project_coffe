import { use, useState } from "react";

function Login(){
    //     variable  function    function  |     object         |
    const [user,      setUser] = useState({email:'', password:''})

    const onChange = (event) =>{
        const value = event.target.value;
        const name = event.target.name;
        setUser({...user, [name]:value})
        //                  משתנה                 
        //      |     object          |
        //  הפעלת פונקציה setUser

        // [name] - הערך של name הוא מפתח
    }
    const onSubmit = (event) => {
        event.preventDefault();
        console.log(user);
        
    }
    return(
        <form onSubmit={onSubmit}>
            <input type="email" required name="email" onChange={onChange} placeholder="your email" style={{direction:'ltr'}}/>
            <input type="password" required name="password" onChange={onChange} placeholder="your password" style={{direction:'ltr'}}/>
            <button>LOGIN</button>
        </form>
    )
}

export default Login;