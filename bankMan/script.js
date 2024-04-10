let msg = document.querySelector("#msg");
let btn = document.querySelector("#btn");
let user_msg = document.querySelector("#user_msg");

// Function to adjust the height of the textarea based on its content
const adjustTextareaHeight = () => {
    user_msg.style.height = "auto";
    user_msg.style.height = user_msg.scrollHeight + "px";
};

const display = () => {    
    user_msg.value = msg.value;
    if(msg.value !== "") {
        btn.disabled=false;
        user_msg.style.backgroundColor = "blueviolet"; 
    }
    msg.value = "";
    adjustTextareaHeight(); // Call the function to adjust textarea height after updating its content
};

// Add event listener to the button for displaying the message
btn.addEventListener("click", display);

// Add event listener to the textarea for adjusting its height as the user types
msg.addEventListener("input", adjustTextareaHeight);



