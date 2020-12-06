
function getCalculator() {
    let weight = document.querySelector('#weight').value;
    // Need to convert values to Int to avaoid concatenating the two 
    let total_height = parseInt(document.querySelector('#height_ft').value) + parseInt(document.querySelector('#height_in').value);
    let age = document.querySelector('#age').value;

   
    


    // Protein Requirements
        // Min
    let calc_protein_min_raw = .36 * weight
    let calc_protein_min = Math.round(calc_protein_min_raw  *10)/10
    let calc_protein__min_display = document.getElementById('p_min')
    calc_protein__min_display.innerHTML = calc_protein_min
        // Max
    let calc_protein_max_raw = .70 * weight
    let calc_protein_max = Math.round(calc_protein_max_raw  *10)/10
    let calc_protein__max_display = document.getElementById('p_max')
    calc_protein__max_display.innerHTML = calc_protein_max



    // BMI = [(lbs/inches^2) * 703]*100
    let bmi_raw = (weight/total_height**2)*703
         // rounding off 1 decimal points:
    bmi = Math.round(bmi_raw * 10) / 10
    let bmi_display = document.getElementById('bmi')
    bmi_display.innerHTML = bmi


    // Calories Burned (using Harris-Benedict Eqation)
        // Men: BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) - (5.677 x age in years)
        // Women: BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) - (4.330 x age in years)

    let weight_kg = weight * .45359237
    let total_height_cm = total_height * 2.54
    

    if (document.querySelector('#sex').value == 'm'){
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * total_height_cm) - (5.677 * age)
     
    }else if (document.querySelector('#sex').value == 'f'){
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * total_height_cm) - (4.330 * age)
    }

    let calories_burned = Math.round(bmr * document.querySelector('#activity_level').value)
    let calories_burned_display = document.getElementById('cal_in')
    calories_burned_display.innerHTML = calories_burned

}


function getNutrients() {
    let food = document.querySelector('#food').value;
    fetch(`https://api.nal.usda.gov/fdc/v1/foods/search?api_key=GofKphqBkpQGGM86CFBqZnG0o0NsRROcWL3aYzzP&query=${food}`)
    .then(response => response.json())
    .then(data => {
        console.log(data)
         
     
// Food Name
let food_display = document.getElementById('fooddisplay')
food_display.innerHTML = data.foods[0].description



// Finding the index that matches the description entered
let l_list = data.foods
let match = 0
for (let i = 0; i< l_list; i++){
    if (data.foods[i].lowercaseDescription == food.toLowerCase()+ ", raw"){
        match = i
    }
}
let l = data.foods[match].foodNutrients.length

// Protein
let p_id = 1003
for (let i = 0; i< l; i++){
    if (data.foods[match].foodNutrients[i].nutrientId == p_id){
        protein = data.foods[match].foodNutrients[i].value 
    }
}
let Protein_display = document.getElementById('protein')
Protein_display.innerHTML = protein


// Carbohydrates
let carb_id = 1005
for (let i = 0; i< l; i++){
    if (data.foods[match].foodNutrients[i].nutrientId == carb_id){
        carbs = data.foods[match].foodNutrients[i].value 
    }
}
let Carbs_display = document.getElementById('carbs')
Carbs_display.innerHTML = carbs

// Calories
let calories_id = 1008
for (let i = 0; i< l; i++){
    if (data.foods[match].foodNutrients[i].nutrientId == calories_id){
        calories = data.foods[match].foodNutrients[i].value 
    }
}
let Calories_display = document.getElementById('calories')
Calories_display.innerHTML = calories

})
}




