/* =====================================
    WEDDING INVITATION
    SCRIPT.JS
===================================== */

document.addEventListener("DOMContentLoaded", function () {

    /*==========================
        BUTTON BUKA UNDANGAN
    ==========================*/

    const openButton = document.getElementById("openInvitation");

    const cover = document.querySelector(".cover");

    openButton.addEventListener("click", function(){

        cover.style.transition="1s";

        cover.style.opacity="0";

        setTimeout(function(){

            cover.style.display="none";

            window.scrollTo({

                top:0,

                behavior:"smooth"

            });

        },1000);

    });

    /*==========================
            COUNTDOWN
    ==========================*/

    const targetDate = new Date("August 8, 2026 08:00:00").getTime();

    function countdown(){

        const now = new Date().getTime();

        const distance = targetDate-now;

        if(distance<0){

            document.getElementById("days").innerHTML="00";

            document.getElementById("hours").innerHTML="00";

            document.getElementById("minutes").innerHTML="00";

            document.getElementById("seconds").innerHTML="00";

            return;

        }

        const days=Math.floor(distance/(1000*60*60*24));

        const hours=Math.floor((distance%(1000*60*60*24))/(1000*60*60));

        const minutes=Math.floor((distance%(1000*60*60))/(1000*60));

        const seconds=Math.floor((distance%(1000*60))/1000);

        document.getElementById("days").innerHTML=days;

        document.getElementById("hours").innerHTML=hours;

        document.getElementById("minutes").innerHTML=minutes;

        document.getElementById("seconds").innerHTML=seconds;

    }

    countdown();

    setInterval(countdown,1000);

    /*==========================
        SCROLL ANIMATION
    ==========================*/

    const sections=document.querySelectorAll(".section");

    function reveal(){

        sections.forEach(section=>{

            const top=section.getBoundingClientRect().top;

            const height=window.innerHeight;

            if(top<height-120){

                section.classList.add("show");

            }

        });

    }

    reveal();

    window.addEventListener("scroll",reveal);

});

/*==========================
    LIGHTBOX
==========================*/

const gallery=document.querySelectorAll(".gallery-grid img");

const lightbox=document.getElementById("lightbox");

const lightboxImage=document.getElementById("lightboxImage");

const closeLightbox=document.getElementById("closeLightbox");

gallery.forEach(img=>{

    img.addEventListener("click",function(){

        lightbox.style.display="flex";

        lightboxImage.src=this.src;

    });

});

closeLightbox.addEventListener("click",function(){

    lightbox.style.display="none";

});