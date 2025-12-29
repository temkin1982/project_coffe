import { Link } from 'react-router-dom'

function Menu(){

    return(
        <div style={{with:'100%', display:'flex', gap:'5%', justifyContent:'space-around', alignItems:'center'}}>
            <Link to='/' ><img src='/coffee.jpg' alt='Logo' style={{width:'50px', borderRadius:'5px'}}/></Link>
            <Link to='/coffee'>הקפה שלנו</Link>
            <Link to='/search'>חיפוש קפה</Link>
            <Link to='/coffee/new'>הוספת קפה</Link>
            <Link to='/login'>כניסה</Link>
            <Link to='/register'>רישום</Link>
            <Link to='/logout'>יציאה</Link>
        </div>
    )
}

export default Menu;