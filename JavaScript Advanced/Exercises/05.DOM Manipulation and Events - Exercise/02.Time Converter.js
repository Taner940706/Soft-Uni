function attachEventsListeners() {


	let day = document.getElementById('days');
    let hour = document.getElementById('hours');
    let minute = document.getElementById('minutes');
    let second = document.getElementById('seconds');

    document.getElementById('daysBtn').addEventListener("click", calc_day);
    document.getElementById('hoursBtn').addEventListener("click", calc_hours);
    document.getElementById('minutesBtn').addEventListener("click", calc_minutes);
    document.getElementById('secondsBtn').addEventListener("click", calc_seconds);
    

    function calc_day(){

    	hour.value = Number(day.value) * 24;
    	minute.value = Number(day.value) * 24 * 60;
    	second.value = Number(day.value) * 24 * 60 * 60;
    }

    function calc_hours(){

    	day.value = Number(hour.value) / 24;
    	minute.value = Number(hour.value) * 60;
    	second.value = Number(hour.value) * 60 * 60;
    }

    function calc_minutes(){

    	day.value = Number(minute.value) / 60 / 24;
    	hour.value = Number(minute.value) / 60;
    	second.value = Number(minute.value) * 60;
    }

    function calc_seconds(){

    	day.value = Number(second.value) / 60 / 60 / 24;
    	hour.value = Number(second.value) / 60 / 60;
    	minute.value = Number(second.value) / 60;
    }

}