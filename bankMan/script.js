let msg=document.querySelector("#msg");
let btn=document.querySelector("#btn");
let user_msg=document.querySelector("#user_msg");

const display=()=>{
    user_msg.value=msg.value;
    msg.value="";
    user_msg.style.backgroundColor="rgb(96, 45, 204)";
}

btn.addEventListener("click",display);