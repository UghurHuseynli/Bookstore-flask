let paparSize = prompt("Kitabın səhifə sayını daxil edin: ");
while (isNaN(paparSize)){
    alert("Xəta baş verdi, zəhmət olmasa ədəd daxil edin.");
    paparSize = prompt("Kitabın səhifə sayını daxil edin: ");
}
let daySize = prompt("Neçə günə bitirməlisiniz? : ");
while(isNaN(daySize) || daySize == 0){
    alert("Xəta baş verdi, zəhmət olmasa ədəd daxil edin.");
    daySize = prompt("Neçə günə bitirməlisiniz? : ");
}
let readPaper = Math.ceil(parseInt(paparSize) / parseInt(daySize));
alert(`Hər gün ən az ${readPaper} səhifə oxumalısınız.`);
console.log(`Səhifə sayı: ${paparSize}\nGün sayı: ${daySize}\nNəticə: ${readPaper}`);