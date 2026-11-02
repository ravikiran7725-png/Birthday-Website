from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Advance Happy Birthday Babyyyy! 🎂</title>
<style>
:root{--pink:#ff5fa2;--purple:#8c52ff;--gold:#ffd166;--glass:rgba(255,255,255,.12)}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;min-height:100vh;color:#fff;font-family:system-ui,-apple-system,Segoe UI,sans-serif;overflow-x:hidden;background:radial-gradient(circle at 15% 20%,#552477 0,transparent 35%),radial-gradient(circle at 85% 80%,#173d73 0,transparent 35%),linear-gradient(135deg,#100b2b,#211044 55%,#090d25)}
#stars,.confetti-layer{position:fixed;inset:0;pointer-events:none;overflow:hidden;z-index:0}
.star{position:absolute;width:3px;height:3px;border-radius:50%;background:#fff;opacity:.7;animation:twinkle 2s infinite alternate}
@keyframes twinkle{to{opacity:.15;transform:scale(.5)}}
main{position:relative;z-index:1}
nav{display:flex;justify-content:space-between;align-items:center;max-width:1100px;margin:auto;padding:22px 24px}
.logo{font-weight:900;letter-spacing:1px;color:#ffd7eb}.pill{border:1px solid #ffffff40;background:#ffffff12;border-radius:99px;padding:9px 15px;color:white}
.hero{min-height:83vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:40px 20px}
.hero-inner{max-width:850px}
.eyebrow{display:inline-block;border:1px solid #ffffff40;background:#ffffff10;border-radius:99px;padding:9px 15px;color:#ffe1f0;font-size:.9rem}
h1{font-size:clamp(3rem,9vw,6.7rem);line-height:.98;margin:24px 0 18px;font-weight:950;letter-spacing:-3px;text-shadow:0 0 35px #ff5fa266}
.gradient{background:linear-gradient(90deg,#fff,#ffc4df,#ffd166,#c8b5ff);-webkit-background-clip:text;background-clip:text;color:transparent}
.subtitle{max-width:610px;margin:0 auto 28px;color:#e7ddfa;font-size:clamp(1rem,2.5vw,1.25rem);line-height:1.7}
.actions{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
button{font:inherit;cursor:pointer;transition:transform .2s,filter .2s}
button:hover{transform:translateY(-3px);filter:brightness(1.1)}
.primary,.secondary{padding:13px 21px;border-radius:14px;font-weight:800}
.primary{border:0;color:#28103d;background:linear-gradient(110deg,#ffd166,#ff83ba);box-shadow:0 10px 30px #ff5fa233}
.secondary{color:white;border:1px solid #ffffff40;background:#ffffff12}
.section{max-width:1000px;margin:0 auto;padding:50px 22px 85px;text-align:center}
.section h2{font-size:clamp(2rem,5vw,3rem);margin:0 0 12px}
.muted{color:#d7cbe9;line-height:1.7}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-top:28px;text-align:left}
.card{padding:24px;border:1px solid #ffffff20;background:var(--glass);border-radius:22px;backdrop-filter:blur(12px);box-shadow:0 14px 45px #0002}
.card .emoji{font-size:2rem}.card h3{margin:12px 0 7px}.card p{color:#dfd4ed;line-height:1.6;margin-bottom:0}
.cake-wrap{margin:30px auto 0;max-width:420px;padding:30px;border-radius:26px;background:#ffffff0d;border:1px solid #ffffff20}
.candles{display:flex;justify-content:center;gap:20px;margin-bottom:-3px;position:relative;z-index:2}
.candle{width:12px;height:44px;border-radius:5px 5px 2px 2px;background:repeating-linear-gradient(45deg,#fff 0 5px,#ff79b5 5px 10px);position:relative}
.flame{position:absolute;width:13px;height:19px;border-radius:80% 20% 70% 30%;background:linear-gradient(#fff7a8,#ff9a3c);top:-20px;left:0;transform:rotate(15deg);box-shadow:0 0 18px #ffbd59;animation:flicker .5s infinite alternate}
@keyframes flicker{to{transform:rotate(-12deg) scale(.85)}}
.cake-top{height:42px;width:220px;margin:auto;background:#ffb6d4;border-radius:50% 50% 12px 12px;border-bottom:7px solid #ed75ac}
.cake-body{height:85px;width:250px;margin:auto;background:linear-gradient(90deg,#ff80b8,#ffb4d2,#ff80b8);border-radius:8px 8px 18px 18px;box-shadow:inset 0 -12px #ed659f}
.cake-plate{height:15px;width:290px;margin:auto;background:linear-gradient(#eee,#aaa);border-radius:50%;box-shadow:0 8px 18px #0003}
#cakeMessage{min-height:28px;color:#ffe2a6;margin:20px 0 0;font-weight:700}
.message{max-width:700px;margin:26px auto 0;padding:30px;border:1px solid #ffffff26;background:linear-gradient(135deg,#ffffff14,#ffffff07);border-radius:24px;display:none;animation:appear .5s ease}
.message.show{display:block}
@keyframes appear{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.message p{font-size:1.15rem;line-height:1.9;color:#f4eafa}
.gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:26px}
.memory{min-height:150px;display:grid;place-items:center;border-radius:18px;border:1px dashed #ffffff55;background:linear-gradient(135deg,#ff83ba33,#8c52ff33);font-size:2.7rem;position:relative;overflow:hidden}
.memory small{position:absolute;bottom:12px;font-size:.8rem;color:#f6e8ff}
footer{text-align:center;padding:28px 15px 45px;color:#bdb0d1}
.balloon{position:fixed;bottom:-150px;width:52px;height:66px;border-radius:50% 50% 45% 45%;opacity:.7;z-index:0;pointer-events:none;animation:floatUp linear forwards}
.balloon:after{content:"";position:absolute;width:1px;height:45px;background:#ffffff77;left:50%;top:64px}
@keyframes floatUp{to{transform:translateY(-125vh) rotate(12deg);opacity:0}}
.confetti{position:fixed;top:-20px;width:9px;height:14px;z-index:5;pointer-events:none;animation:fall linear forwards}
@keyframes fall{to{transform:translateY(110vh) rotate(800deg);opacity:.2}}
@media(max-width:600px){nav{padding:18px}.logo{font-size:.9rem}h1{letter-spacing:-1.5px}.gallery{grid-template-columns:1fr}.memory{min-height:120px}.cake-wrap{padding:22px 10px}.cake-body{width:210px}.cake-top{width:185px}.cake-plate{width:240px}}
</style>
</head>
<body>
<div id="stars"></div><div class="confetti-layer" id="confetti"></div>
<main>
<nav><div class="logo">✨ BIRTHDAY MAGIC</div><div class="pill">A day made for you ♡</div></nav>
<section class="hero">
 <div class="hero-inner">
  <span class="eyebrow">🎉 28 days 🎉</span>
  <h1><span class="gradient">Advance Happy Birthday!</span><br>🌟</h1>
  <p class="subtitle">Another year of becoming more wonderful.</p>
  <div class="actions"><button class="primary" onclick="celebrate()">🎊 Start the celebration</button><button class="secondary" onclick="openMessage()">💌 Open your surprise</button></div>
 </div>
</section>
<section class="section">
 <h2>Make a wish ✨</h2><p class="muted">One little cake, a thousand wishes, and a whole lot of love.</p>
 <div class="cake-wrap">
  <div class="candles"><div class="candle"><span class="flame"></span></div><div class="candle"><span class="flame"></span></div><div class="candle"><span class="flame"></span></div></div>
  <div class="cake-top"></div><div class="cake-body"></div><div class="cake-plate"></div>
  <button class="primary" style="margin-top:24px" onclick="blowCandles in advance()">🌬️ Blow out the candles in advance</button>
 </div>
</section>
<section class="section">
 </div>
 <div class="message" id="surprise"><div style="font-size:2.5rem">💌</div><h2>A little note for you</h2><p>Advance Happy Birthday to someone truly special! The one who always with me in every time and the one who loves me unconditionally the one who is their for me. ❤️</p><button class="secondary" onclick="celebrate()">Send some birthday magic  ✨</button></div>
</section>
</main>
<script>
const starField=document.getElementById('stars');
for(let i=0;i<95;i++){let s=document.createElement('i');s.className='star';s.style.left=Math.random()*100+'%';s.style.top=Math.random()*100+'%';s.style.animationDelay=Math.random()*3+'s';s.style.opacity=.2+Math.random()*.8;starField.appendChild(s)}
function confettiBurst(count=150){const layer=document.getElementById('confetti');for(let i=0;i<count;i++){let c=document.createElement('i');c.className='confetti';c.style.left=Math.random()*100+'vw';c.style.background=['#ff5fa2','#ffd166','#8c52ff','#68e1fd','#9cffac'][Math.floor(Math.random()*5)];c.style.animationDuration=(2+Math.random()*3)+'s';c.style.animationDelay=Math.random()*.7+'s';c.style.transform='rotate('+Math.random()*360+'deg)';layer.appendChild(c);setTimeout(()=>c.remove(),6000)}}
function floatBalloons(){for(let i=0;i<12;i++){let b=document.createElement('div');b.className='balloon';b.style.left=Math.random()*100+'vw';b.style.background=['#ff5fa2','#ffd166','#8c52ff','#68e1fd','#9cffac'][i%5];b.style.animationDuration=(7+Math.random()*7)+'s';b.style.animationDelay=Math.random()*2+'s';document.body.appendChild(b);setTimeout(()=>b.remove(),16000)}}
function celebrate(){confettiBurst();floatBalloons()}
function openMessage(){document.getElementById('surprise').classList.add('show');document.getElementById('surprise').scrollIntoView({behavior:'smooth',block:'center'});confettiBurst(80)}
function blowCandles(){document.querySelectorAll('.flame').forEach(f=>f.style.display='none');document.getElementById('cakeMessage').textContent='✨ Wish sent to the universe! May it come true. ✨';confettiBurst(100)}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

if __name__ == "__main__":
    print("Birthday website is running at http://127.0.0.1:5000")
    app.run(debug=True)
