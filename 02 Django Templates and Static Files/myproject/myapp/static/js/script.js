document.addEventListener('DOMContentLoaded', function() {
       const container = document.querySelector('.container');
    container.style.backgroundColor = 'lightblue';

    
    container.addEventListener('click', function() {
               container.style.backgroundColor = getRandomColor(); // You can define your color or use a function to generate a random color
    });

    function getRandomColor() {
        const letters = '0123456789ABCDEF';  
        let color = '#';      
        for (let i = 0; i < 6; i++) {  
            color += letters[Math.floor(Math.random() * 16)];        }
    
        return color;  
 }
    
});
