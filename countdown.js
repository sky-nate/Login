let count = 60;
const timer = setInterval(function(){
    count--;
    console.log("count");

    if (count ===0){
        clearInterval(timer);
        console.log("Time is up gang");
    }

}, 1000);