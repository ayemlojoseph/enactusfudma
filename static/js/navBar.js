const navSlide = () =>{
    const hamburger = document.querySelector('.hamburger');
    const nav = document.querySelector('.navList');

    //selcting all the navList for the animation
    const navList = document.querySelectorAll('.navList li');

    hamburger.addEventListener('click', ()=>{

        //Toggle nav
        nav.classList.toggle('navActive');
        
         //animation 
        navList.forEach((link, index)=>{
            if (link.style.animation){
                link.style.animation = '';
            }else{
            link.style.animation = `navLinkFade 0.5s ease forwards ${index/7 +0.5}s`
                //0.5 adds initial delay
                //the division will make sure one link slide before the other in sequaltial order
            }//the if statememts will allow this to work without a refresh
        })

        //burger cross
        hamburger.classList.toggle('toggleBurger')
    })

   
}

navSlide();
