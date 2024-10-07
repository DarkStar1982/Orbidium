function get_center_point(canvas)
{
    if (window.devicePixelRatio > 1) {
        return [canvas.width/4, canvas.height/4]
    }
    else return [canvas.width/2, canvas.height/2]
}
function drawCenter(canvas) {

    const ctx = canvas.getContext("2d");
    ctx.beginPath();
    //retina screen only
    ctx.arc(canvas.width / 4, canvas.height/ 4, 20, 0, 2*Math.PI);
    ctx.fillStyle = 'yellow';
    ctx.fill();
    ctx.stroke();
}

function draw_y_axis(canvas)
{
    var center_point= get_center_point(canvas);
    var center_x = center_point[0];
    var center_y = center_point[1];
    const ctx = canvas.getContext("2d");
    ctx.strokeStyle = "blue";
    ctx.beginPath();
    ctx.moveTo(center_x, 50);
    ctx.lineTo(center_x, 600);
    ctx.stroke();
}

function draw_x_axis(canvas)
{
    var center_point= get_center_point(canvas);
    var center_x = center_point[0];
    var center_y = center_point[1];
    const ctx = canvas.getContext("2d");
    ctx.strokeStyle = "blue";
    ctx.beginPath();
    ctx.moveTo(50, center_y);
    ctx.lineTo(1200, center_y);
    ctx.stroke();
}

function draw_asteroid(canvas, asteroid, color)
{
    var au=149.6;
    var eccentricity = asteroid.eccentricity
    var semiMajorAxis = asteroid.semimajor_a*au;
    var argPeriapsis = asteroid.argument_perihelion;
    var angle = asteroid.argument_perihelion*(Math.PI/180);
    drawOrbitEllipse(canvas, semiMajorAxis, argPeriapsis, eccentricity, color, true);

}

function drawOrbitEllipse(canvas, semiMajorAxis, argPeriapsis, eccentricity, p_color, is_asteroid=false)
{

    const ctx = canvas.getContext("2d");
    var center_point= get_center_point(canvas);
    var sunX = center_point[0];
    var sunY = center_point[1];

    const focalDistance = semiMajorAxis * eccentricity;
    const semiMinorAxis = semiMajorAxis * Math.sqrt(1 - eccentricity * eccentricity);
  
    // Calculate center of the ellipse
    const centerX = sunX + focalDistance * Math.cos(argPeriapsis);
    const centerY = sunY + focalDistance * Math.sin(argPeriapsis);
  
    if (is_asteroid) ctx.lineWidth=1;
    else ctx.lineWidth=3; 

    // Draw the elliptical orbit
    ctx.beginPath();
    ctx.ellipse(centerX, centerY, semiMajorAxis, semiMinorAxis, argPeriapsis, 0, 2 * Math.PI);
    ctx.strokeStyle = p_color;
    ctx.stroke();
}

function draw() {
    
    const canvas = document.getElementById("canvasMap");
    const ctx = canvas.getContext("2d");
    ctx.canvas.width  = window.innerWidth;
    ctx.canvas.height = window.innerHeight;

    //setup page - retina screen only!
    if (window.devicePixelRatio > 1) {
        var canvasWidth = canvas.width;
        var canvasHeight = canvas.height;

        canvas.width = canvasWidth * window.devicePixelRatio;
        canvas.height = canvasHeight * window.devicePixelRatio;
        canvas.style.width = canvasWidth + "px";
        canvas.style.height = canvasHeight + "px";
        ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
    }

    drawCenter(canvas);
    draw_y_axis(canvas);
    draw_x_axis(canvas);


    //load dangerous asteroids
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        // What to do when the response is ready
        data = JSON.parse(this.responseText);
        neos = data["pha"]
        mbas = data["mba"]
        for (a in neos)
        {
            draw_asteroid(canvas, neos[a], "yellow");
        }
        for (b in mbas)
        {
            draw_asteroid(canvas, mbas[b], "white");
        }
        //Draw inner planets
        drawOrbitEllipse(canvas, 149.6, 114.20783, 0.0167086, "green", false);
        drawOrbitEllipse(canvas, 108.21, 54.884, 0.006772, "grey", false);
        drawOrbitEllipse(canvas, 57.91, 29.124, 0.20563, "orange", false);
        drawOrbitEllipse(canvas, 227.93, 286.50, 0.0934, "red", false);           
    }
    xhttp.open("GET", "get_data", true);
    xhttp.send();
    
}