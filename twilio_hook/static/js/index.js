let signup = document.querySelector(".signup");
let login = document.querySelector(".login");
let slider = document.querySelector(".slider");
let formSection = document.querySelector(".form-section");

signup.addEventListener("click", () => {
	slider.classList.add("moveslider");
	formSection.classList.add("form-section-move");
});

login.addEventListener("click", () => {
	slider.classList.remove("moveslider");
	formSection.classList.remove("form-section-move");
});

sendotp = () => {
    document.getElementById("password").style.display = "block";
    document.getElementById("sendotp").style.display = "none";
    document.getElementById("verify").style.display = "block";
    const phoneNumber = phoneInput.getNumber();
    console.log(phoneNumber);
    
}
verify= ()=>{
    console.log("dd")
    window.location.replace("/home.html")
}