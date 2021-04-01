function comma(value){
    let digit = new Intl.NumberFormat({minimumFractionDigits: 3}); // minimumFractionDigits default 3
    return digit.format(value)
}
