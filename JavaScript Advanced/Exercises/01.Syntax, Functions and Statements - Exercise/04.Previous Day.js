function previous_day(year, month, day) {
    let previousday = new Date(year, month, day - 1);
    let newYear = previousday.getFullYear();
    let newMonth = previousday.getMonth() - 1;
    let newDate = previousday.getDate();
    console.log(`${newYear}-${newMonth + 1}-${newDate}`);
}