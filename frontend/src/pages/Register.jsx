import { use, useState } from "react";

function Register(){

    const [user,setUser] = useState({name:'', phone:'', email:'', password:'', role:'regular'})
    const [password2, setPassword2] = useState('')

    const onChange = (event) =>{

        const value = event.target.value;
        const name = event.target.name;
        const checked = event.target.checked;
        console.log(value, name, checked);
        
        setUser({...user, [name]:value})
    }
    const onSubmit = (event) => {
        event.preventDefault();
        console.log(user);
        
    }
    return(
        <form onSubmit={onSubmit}>
            <input type="text" required name="name" value={user.name} onChange={onChange} placeholder="your name" />
            <input type="tel" required name="phone" value={user.phone} onChange={onChange} placeholder="your phone" style={{direction:'ltr'}}/>
            <input type="email" required name="email" value={user.email} onChange={onChange} placeholder="your email" style={{direction:'ltr'}}/>
            <input type="password" required name="password" value={user.password} onChange={onChange} placeholder="your password" style={{direction:'ltr'}}/>
            <input type="password" required name="password2" value={user.password} onChange={onChange} placeholder="your password" style={{direction:'ltr'}}/>
            <br/>
            <label htmlFor="regular">משתמש רגיל</label><input type="radio" name="role" id="regular" value="regular" onChange={onChange}/>
            <label htmlFor="admin">מנהל</label><input type="radio" name="role" id="admin" value="admin" onChange={onChange}/>
         <br/>
            <button>Register</button>
        </form>
    )
}

export default Register;