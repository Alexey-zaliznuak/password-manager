document.addEventListener('click', event => {
    const element = event.target;
    const fileinput = element.classList.contains('img');

    if (fileinput) {
        var FR = new FileReader();
        var myImage = document.querySelector(".img");
        FR.onload = function (event){
            console.log("fffffffffffffffffffffff")
            var contents = event.target.result;
            myImage.src = contents;
        }
        //FR.readAsDataURL(document.querySelector(".inputfile"));
        console.log()
        }
    else {
        console.log(fileinput)
        }
    }
)