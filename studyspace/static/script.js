document.addEventListener('DOMContentLoaded', () => {

    //StopWatch
    const p = document.getElementById('sec');
    const mm = document.getElementById('min');
    const hm = document.getElementById('hr');
    const ele = document.getElementById('play'); 
    const pl = document.getElementById('playarrow');
    const re = document.getElementById('record');
    const r = document.getElementById('renew');
    const tab = document.getElementById('tab');

    if (document.getElementById('renew')) {
        
        r.addEventListener('click', () => {
            count = 0;
            clearInterval(intervalId);
            hm.textContent = '00';
            mm.textContent = '00';
            p.textContent = '00';
            
            if (ele.textContent === 'pause') {
                ele.textContent = 'play_arrow';
            }
            let tab = document.getElementById('tab');
            tab.textContent = null;
        });
    }


    function fun() {
        count = count + 1;
        let seconds = count % 60;
        let minutes = Math.floor((count/60) % 60);
        let hours = Math.floor(count/3600);
         
        console.log(count);
        
        let t = null;
        let s = null;
        let h = null;
        if (seconds < 10) {
            t = '0'+seconds;
            p.textContent = t;
        } else {
            p.textContent = seconds;
        }
        if (minutes < 10) {
            s = '0'+minutes;
            mm.textContent = s;
        } else {
            mm.textContent = minutes;
        } 
        if (hours < 10) {
            h = '0'+hours;
            hm.textContent = h;
        } else {
            hm.textContent = hours;
        }
        return count;
    }
    

    if (document.getElementById('playarrow')) {
        
        pl.addEventListener('click', () => {
           
            if (ele.textContent === 'play_arrow') {
                intervalId = setInterval(fun, 1000);
                console.log('play button clicked!!');
                ele.textContent = 'pause';
                
            } else {
                ele.textContent = 'play_arrow';
                console.log('stop clicked!!');
                clearInterval(intervalId);
            }
        });
    }

    if (document.getElementById('record')) {
        
        let c = 0;
        re.addEventListener('click', () => {
            
            const cr = document.createElement('tr');
            const crr = document.createElement('th');
            const crd = document.createElement('td');
            crr.scope = 'row';
            c = c + 1;
            crr.textContent = c;
            crd.textContent = hm.textContent+':'+mm.textContent+':'+p.textContent;
            cr.appendChild(crr);
            cr.appendChild(crd);
            tab.appendChild(cr);
        });
    }
    
});


var count = 0;
let intervalId = null;




