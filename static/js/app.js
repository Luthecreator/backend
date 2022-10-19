// create function
const navSlide = function(){
    // select burger div and nav div from the DOM
    const burger = document.querySelector(".burger");
    console.log(burger)
    const nav = document.querySelector(".nav-links");
     console.log(nav)
    // select all the links
    const navLinks = nav.querySelectorAll(".nav-links li");
    console.log(navLinks)  

    // Toggle navigation
burger.addEventListener('click',function(){
    nav.classList.toggle("nav-active");

    navLinks.forEach((link,index) => {
       // console.log(link, index)
       if(link.style.animation === true){
           link.style.animation = '';
       }else{
           // Animate links
           link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.2}s`
       }
       
    });
    //burger Animation
    burger.classList.toggle("toggle")
 });
}
navSlide()

// PRODUCT FILTER SECTION STARTS 19/07/2022

const btns = document.querySelectorAll(".btn");
console.log(btns)
const blogItems = document.querySelectorAll(".card-itms");
console.log(blogItems)

for(let i=0 ; i < btns.length; i++){
    btns[i].addEventListener('click',function(e){
        e.preventDefault()
        const filter = e.target.dataset.filter
        console.log(filter)

        // create foreach loop
        blogItems.forEach((blogItem) =>{
            if(filter === 'all'){
                blogItem.style.display = 'flex';

                //  btns[0].classList.add('active')
                //  btns[0].style.color = 'white'

                //  btns[1].classList.remove('active')
                //  btns[2].classList.remove('active')
                //  btns[3].classList.remove('active')
                //  btns[4].classList.remove('active')
            }
            else{

                // btns[0].classList.remove('active')
                // btns[0].style.color = 'rgb(75, 62, 62)'


                if(blogItem.classList.contains(filter)){
                    blogItem.style.display = 'flex';
                   
                    //  if(btns[1] === e.target){
                    //      btns[1].classList.add('active')
                    //      btns[1].style.color = 'white'
                    //  }else{
                    //     btns[1].classList.remove('active')
                    //     btns[0].style.color = '#4b3e3e'
                    //  }

                    //  if(btns[2] === e.target){
                    //      btns[2].classList.add('active')
                    //      btns[2].style.color = 'white'
                    //  }else{
                    //      btns[2].classList.remove('active')
                    //      btns[0].style.color = '#4b3e3e'
                    //  }

                    //  if(btns[3] === e.target){
                    //      btns[3].classList.add('active')
                    //      btns[3].style.color = 'white'
                    //  }else{
                    //      btns[3].classList.remove('active')
                    //      btns[0].style.color = '#4b3e3e'
                    //  }

                    //  if(btns[4] === e.target){
                    //      btns[4].classList.add('active')
                    //      btns[4].style.color = 'white'
                    //  }else{
                    //      btns[4].classList.remove('active')
                    //      btns[0].style.color = '#4b3e3e'
                    //  }

                    
                }
                else{
                blogItem.style.display = 'none';
                }
            }
           
        })
    })
}

// PRODUCT FILTER SECTION ENDS

// SEARCH FILTER STARTS HERE

const search = document.querySelector('#search');
console.log(search)
search.addEventListener("keyup", (e) => {
    e.preventDefault()
    const searchValue = search.value.toLowerCase().trim();
    console.log(searchValue)

    // loop through blog category
    for(let i = 0; i < blogItems.length; i++) {
        console.log(blogItems)
        if(blogItems[i].classList.contains(searchValue)){
            blogItems[i].style.display = 'flex';
        }else if(searchValue === ""){
            blogItems[i].style.display = 'flex';
        }else{
            blogItems[i].style.display = 'none';
        }
    }



})

// SEARCH FILTER ENDS HERE

