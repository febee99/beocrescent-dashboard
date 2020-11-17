(window.webpackJsonp=window.webpackJsonp||[]).push([[6],{221:function(t,e,n){"use strict";n.r(e);var r={name:"CardComponent",props:{title:{type:String,default:null},icon:{type:String,default:null},headerIcon:{type:String,default:null}},methods:{headerIconClick:function(){this.$emit("header-icon-click")}}},l=n(22),component=Object(l.a)(r,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"card"},[t.title?n("header",{staticClass:"card-header"},[n("p",{staticClass:"card-header-title"},[t.icon?n("b-icon",{attrs:{icon:t.icon,"custom-size":"default"}}):t._e(),t._v("\n      "+t._s(t.title)+"\n    ")],1),t._v(" "),t.headerIcon?n("a",{staticClass:"card-header-icon",attrs:{href:"#","aria-label":"more options"},on:{click:function(e){return e.preventDefault(),t.headerIconClick(e)}}},[n("b-icon",{attrs:{icon:t.headerIcon,"custom-size":"default"}})],1):t._e()]):t._e(),t._v(" "),n("div",{staticClass:"card-content"},[t._t("default")],2)])}),[],!1,null,null,null);e.default=component.exports},222:function(t,e,n){"use strict";n.r(e);n(228);var r=n(221),l={name:"CardWidget",components:{GrowingNumber:n(225).default,CardComponent:r.default},props:{description:{type:String,default:""},icon:{type:String,default:null},number:{type:Number,default:0},prefix:{type:String,default:null},suffix:{type:String,default:null},label:{type:String,default:null},type:{type:String,default:null}}},o=n(22),component=Object(o.a)(l,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("card-component",[n("div",{staticClass:"level"},[n("div",{staticClass:"level-item"},[n("div",{staticClass:"is-widget-label"},[n("h3",{staticClass:"subtitle is-spaced is-size-6-touch"},[t._v("\n                    "+t._s(t.label)+"\n                    "),n("b-tooltip",{attrs:{label:t.description,type:"is-light",position:"is-top",active:t.active}},[n("sup",[n("b-icon",{attrs:{icon:"help-circle-outline",size:"is-small",type:"is-grey"}})],1)])],1),t._v(" "),n("h1",{staticClass:"title is-size-5-touch"},[n("growing-number",{attrs:{value:t.number,prefix:t.prefix,suffix:t.suffix}})],1)]),t._v(" "),t.icon?n("div",{staticClass:"level-item has-widget-icon"},[n("div",{staticClass:"is-widget-icon"},[n("b-icon",{attrs:{icon:t.icon,size:"is-large",type:t.type}})],1)]):t._e()])])])}),[],!1,null,null,null);e.default=component.exports;installComponents(component,{GrowingNumber:n(225).default,CardComponent:n(221).default})},223:function(t,e,n){"use strict";n.r(e);var r={extends:n(226).c,props:["chartData","options"],methods:{},mounted:function(){this.renderChart(this.chartData,this.options)}},l=n(22),component=Object(l.a)(r,void 0,void 0,!1,null,null,null);e.default=component.exports},224:function(t,e,n){"use strict";n.r(e);var r={extends:n(226).d,props:["chartData","options"],methods:{},mounted:function(){this.renderChart(this.chartData,this.options)}},l=n(22),component=Object(l.a)(r,void 0,void 0,!1,null,null,null);e.default=component.exports},225:function(t,e,n){"use strict";n.r(e);n(228),n(56);var r=n(365),l=n.n(r),o={name:"GrowingNumber",props:{prefix:{type:String,default:null},suffix:{type:String,default:null},value:{type:Number,default:0},duration:{type:Number,default:500}},data:function(){return{newValue:0,step:0}},computed:{newValueFormatted:function(){return this.newValue<1e3?this.newValue:l()(this.newValue).format("0,0")}},watch:{value:function(){this.growInit()}},mounted:function(){this.growInit()},methods:{growInit:function(){var t=this.value/(this.duration/25);this.grow(t)},grow:function(t){var e=this,n=Math.ceil(this.newValue+t);if(n>this.value)return this.newValue=this.value,!1;this.newValue=n,setTimeout((function(){e.grow(t)}),25)}}},c=n(22),component=Object(c.a)(o,(function(){var t=this.$createElement;return(this._self._c||t)("div",[this._v(this._s(this.prefix)+this._s(this.newValueFormatted)+this._s(this.suffix))])}),[],!1,null,null,null);e.default=component.exports},227:function(t,e,n){"use strict";var base="https://qju04f7u0a.execute-api.ap-southeast-1.amazonaws.com/dev";e.a={BASE:base,TABLEVISION:"/tables",TABLEVISIONSTATS:"/stats",RFIDFSRVISIO:"/rfid_fsr",RFIDTRAYINOUT:"/tray_in_out",RFIDTRAYIN:"/tray_in",RETURNDISTRVISION:"/g6trayreturndistr",STALLTOTALVISION:"/g6total",BARCHART:"/g6barchart",G6OVERVIEW:"/g6overview",OVERVIEW2:"/overview2",OVERVIEW:"/overview/tray_return"}},364:function(t,e,n){"use strict";var r=n(2),l=n(39),o=n(367),c=n(159),d=n(5),f=1..toFixed,h=Math.floor,j=function(t,e,n){return 0===e?n:e%2==1?j(t,e-1,n*t):j(t*t,e/2,n)};r({target:"Number",proto:!0,forced:f&&("0.000"!==8e-5.toFixed(3)||"1"!==.9.toFixed(0)||"1.25"!==1.255.toFixed(2)||"1000000000000000128"!==(0xde0b6b3a7640080).toFixed(0))||!d((function(){f.call({})}))},{toFixed:function(t){var e,n,r,d,f=o(this),v=l(t),data=[0,0,0,0,0,0],m="",y="0",I=function(t,e){for(var n=-1,r=e;++n<6;)r+=t*data[n],data[n]=r%1e7,r=h(r/1e7)},C=function(t){for(var e=6,n=0;--e>=0;)n+=data[e],data[e]=h(n/t),n=n%t*1e7},R=function(){for(var t=6,s="";--t>=0;)if(""!==s||0===t||0!==data[t]){var e=String(data[t]);s=""===s?e:s+c.call("0",7-e.length)+e}return s};if(v<0||v>20)throw RangeError("Incorrect fraction digits");if(f!=f)return"NaN";if(f<=-1e21||f>=1e21)return String(f);if(f<0&&(m="-",f=-f),f>1e-21)if(n=(e=function(t){for(var e=0,n=t;n>=4096;)e+=12,n/=4096;for(;n>=2;)e+=1,n/=2;return e}(f*j(2,69,1))-69)<0?f*j(2,-e,1):f/j(2,e,1),n*=4503599627370496,(e=52-e)>0){for(I(0,n),r=v;r>=7;)I(1e7,0),r-=7;for(I(j(10,r,1),0),r=e-1;r>=23;)C(1<<23),r-=23;C(1<<r),I(1,1),C(2),y=R()}else I(0,n),I(1<<-e,0),y=R()+c.call("0",v);return y=v>0?m+((d=y.length)<=v?"0."+c.call("0",v-d)+y:y.slice(0,d-v)+"."+y.slice(d-v)):m+y}})},366:function(t,e,n){var map={"./af":229,"./af.js":229,"./ar":230,"./ar-dz":231,"./ar-dz.js":231,"./ar-kw":232,"./ar-kw.js":232,"./ar-ly":233,"./ar-ly.js":233,"./ar-ma":234,"./ar-ma.js":234,"./ar-sa":235,"./ar-sa.js":235,"./ar-tn":236,"./ar-tn.js":236,"./ar.js":230,"./az":237,"./az.js":237,"./be":238,"./be.js":238,"./bg":239,"./bg.js":239,"./bm":240,"./bm.js":240,"./bn":241,"./bn-bd":242,"./bn-bd.js":242,"./bn.js":241,"./bo":243,"./bo.js":243,"./br":244,"./br.js":244,"./bs":245,"./bs.js":245,"./ca":246,"./ca.js":246,"./cs":247,"./cs.js":247,"./cv":248,"./cv.js":248,"./cy":249,"./cy.js":249,"./da":250,"./da.js":250,"./de":251,"./de-at":252,"./de-at.js":252,"./de-ch":253,"./de-ch.js":253,"./de.js":251,"./dv":254,"./dv.js":254,"./el":255,"./el.js":255,"./en-au":256,"./en-au.js":256,"./en-ca":257,"./en-ca.js":257,"./en-gb":258,"./en-gb.js":258,"./en-ie":259,"./en-ie.js":259,"./en-il":260,"./en-il.js":260,"./en-in":261,"./en-in.js":261,"./en-nz":262,"./en-nz.js":262,"./en-sg":263,"./en-sg.js":263,"./eo":264,"./eo.js":264,"./es":265,"./es-do":266,"./es-do.js":266,"./es-mx":267,"./es-mx.js":267,"./es-us":268,"./es-us.js":268,"./es.js":265,"./et":269,"./et.js":269,"./eu":270,"./eu.js":270,"./fa":271,"./fa.js":271,"./fi":272,"./fi.js":272,"./fil":273,"./fil.js":273,"./fo":274,"./fo.js":274,"./fr":275,"./fr-ca":276,"./fr-ca.js":276,"./fr-ch":277,"./fr-ch.js":277,"./fr.js":275,"./fy":278,"./fy.js":278,"./ga":279,"./ga.js":279,"./gd":280,"./gd.js":280,"./gl":281,"./gl.js":281,"./gom-deva":282,"./gom-deva.js":282,"./gom-latn":283,"./gom-latn.js":283,"./gu":284,"./gu.js":284,"./he":285,"./he.js":285,"./hi":286,"./hi.js":286,"./hr":287,"./hr.js":287,"./hu":288,"./hu.js":288,"./hy-am":289,"./hy-am.js":289,"./id":290,"./id.js":290,"./is":291,"./is.js":291,"./it":292,"./it-ch":293,"./it-ch.js":293,"./it.js":292,"./ja":294,"./ja.js":294,"./jv":295,"./jv.js":295,"./ka":296,"./ka.js":296,"./kk":297,"./kk.js":297,"./km":298,"./km.js":298,"./kn":299,"./kn.js":299,"./ko":300,"./ko.js":300,"./ku":301,"./ku.js":301,"./ky":302,"./ky.js":302,"./lb":303,"./lb.js":303,"./lo":304,"./lo.js":304,"./lt":305,"./lt.js":305,"./lv":306,"./lv.js":306,"./me":307,"./me.js":307,"./mi":308,"./mi.js":308,"./mk":309,"./mk.js":309,"./ml":310,"./ml.js":310,"./mn":311,"./mn.js":311,"./mr":312,"./mr.js":312,"./ms":313,"./ms-my":314,"./ms-my.js":314,"./ms.js":313,"./mt":315,"./mt.js":315,"./my":316,"./my.js":316,"./nb":317,"./nb.js":317,"./ne":318,"./ne.js":318,"./nl":319,"./nl-be":320,"./nl-be.js":320,"./nl.js":319,"./nn":321,"./nn.js":321,"./oc-lnc":322,"./oc-lnc.js":322,"./pa-in":323,"./pa-in.js":323,"./pl":324,"./pl.js":324,"./pt":325,"./pt-br":326,"./pt-br.js":326,"./pt.js":325,"./ro":327,"./ro.js":327,"./ru":328,"./ru.js":328,"./sd":329,"./sd.js":329,"./se":330,"./se.js":330,"./si":331,"./si.js":331,"./sk":332,"./sk.js":332,"./sl":333,"./sl.js":333,"./sq":334,"./sq.js":334,"./sr":335,"./sr-cyrl":336,"./sr-cyrl.js":336,"./sr.js":335,"./ss":337,"./ss.js":337,"./sv":338,"./sv.js":338,"./sw":339,"./sw.js":339,"./ta":340,"./ta.js":340,"./te":341,"./te.js":341,"./tet":342,"./tet.js":342,"./tg":343,"./tg.js":343,"./th":344,"./th.js":344,"./tk":345,"./tk.js":345,"./tl-ph":346,"./tl-ph.js":346,"./tlh":347,"./tlh.js":347,"./tr":348,"./tr.js":348,"./tzl":349,"./tzl.js":349,"./tzm":350,"./tzm-latn":351,"./tzm-latn.js":351,"./tzm.js":350,"./ug-cn":352,"./ug-cn.js":352,"./uk":353,"./uk.js":353,"./ur":354,"./ur.js":354,"./uz":355,"./uz-latn":356,"./uz-latn.js":356,"./uz.js":355,"./vi":357,"./vi.js":357,"./x-pseudo":358,"./x-pseudo.js":358,"./yo":359,"./yo.js":359,"./zh-cn":360,"./zh-cn.js":360,"./zh-hk":361,"./zh-hk.js":361,"./zh-mo":362,"./zh-mo.js":362,"./zh-tw":363,"./zh-tw.js":363};function r(t){var e=l(t);return n(e)}function l(t){if(!n.o(map,t)){var e=new Error("Cannot find module '"+t+"'");throw e.code="MODULE_NOT_FOUND",e}return map[t]}r.keys=function(){return Object.keys(map)},r.resolve=l,t.exports=r,r.id=366},367:function(t,e,n){var r=n(23);t.exports=function(t){if("number"!=typeof t&&"Number"!=r(t))throw TypeError("Incorrect invocation");return+t}},369:function(t,e,n){"use strict";n.r(e);n(364),n(57);var r=n(222),l=n(221),o=(n(223),n(227)),c=(n(224),{components:{CardWidget:r.default,CardComponent:l.default},computed:{selectedDate:function(){return this.date?this.date.getFullYear()+"-"+(parseInt(this.date.getMonth())+1)+"-"+this.date.getDate():"2020-10-12"}},data:function(){var t=new Date;return console.log("today is :"+t),{rfidFsrAPIStatus:"Offline",rfidTrayInStatus:"Offline",rfidTrayIn:[],rfidFsrTable:[],TrayIn:[],loaded:!1,rfid_loaded:!1,interval:null,cleanerReturn:0,selfReturn:0,date:new Date,minDate:new Date(t.getFullYear()-80,t.getMonth(),t.getDate()),maxDate:new Date(t.getFullYear()+18,t.getMonth(),t.getDate()),nanyuanReturns:{labels:["Patrons Return Count","Cleaner Return Count"],datasets:[{backgroundColor:["#ee4350","#409cd2"],pointBackgroundColor:"white",borderWidth:1,pointBorderColor:"#249EBF",data:[]}]},cleanerReturnInsights:{labels:["05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"],datasets:[{label:"Tray OUT",BackgroundColor:"white",borderWidth:3,borderColor:"#ef4250",pointBorderColor:"#249EBF",data:[]},{label:"Tray IN",BackgroundColor:"#white",borderWidth:3,borderColor:"#7AD7F0",pointBorderColor:"#7AD7F0",data:[]}]}}},watch:{rfidFsrTable:function(){this.$refs.nanyuanLineChart.renderChart(this.cleanerReturnInsights)},rfidTrayIn:function(){this.$refs.nanyuanPieChart.renderChart(this.nanyuanReturns)},date:function(){this.getFsrRfidData(),this.getRfidTrayIn()}},methods:{startAPIPolling:function(t){t?(this.getFsrRfidData(),this.getRfidTrayIn()):clearInterval(this.interval)},getFsrRfidData:function(){var t=this;this.cleanerReturnInsights.datasets[0].data=[],this.cleanerReturnInsights.datasets[1].data=[];this.$axios.get(o.a.BASE+o.a.RFIDFSRVISIO).then((function(e){var data=e.data,n=t.selectedDate;console.log(n);var r=data[n];console.log(Object.keys(r));for(var l=0,o=Object.keys(r);l<o.length;l++){var time=o[l];console.log(time);var c=r[time];t.rfidFsrTable.push(c),t.cleanerReturnInsights.datasets[0].data.push(c)}t.rfidFsrAPIStatus="LIVE"})),this.$axios.get(o.a.BASE+o.a.RFIDTRAYIN).then((function(e){var data=e.data;console.log(data);var n=data[t.selectedDate];console.log(t.selectedDate),console.log(Object.keys(n));for(var r=0,l=Object.keys(n);r<l.length;r++){var time=l[r];console.log(time);var o=n[time];t.TrayIn.push(o),console.log("HELLO"),console.log(t.TrayIn),t.cleanerReturnInsights.datasets[1].data.push(o)}t.rfidFsrAPIStatus="LIVE"})).catch((function(e){if(t.rfidFsrAPIStatus="Offline",t.rfidFsrTable=[],null!=e.response){var n=e.response.data;t.toastAlert(n.message,"is-danger",5e3),console.log("nanyuan "+n.message)}else"Offline"!=t.rfidFsrAPIStatus&&(t.toastAlert(e,"is-danger",5e3),console.log("nanyuan "+e))}))},getRfidTrayIn:function(){var t=this;console.log(o.a.RFIDTRAYINOUT);this.$axios.get(o.a.BASE+o.a.RFIDTRAYINOUT).then((function(e){var data=e.data,n=data.CleanerReturn,r=data.SelfReturn;console.log(n),console.log(r);var l=r+n;t.cleanerReturn=parseFloat(n/l*100).toFixed(2),t.selfReturn=parseFloat(r/l*100).toFixed(2);t.nanyuanReturns.datasets[0].data=[r,n],t.rfidTrayIn.push(0),t.rfidFsrAPIStatus="LIVE"})).catch((function(e){if(t.rfidTrayInStatus="Offline",t.getRfidTrayIn1=[],null!=e.response){var n=e.response.data;t.toastAlert(n.message,"is-danger",5e3),console.log("nanyuan "+n.message)}else"Offline"!=t.rfidFsrAPIStatus&&(t.toastAlert(e,"is-danger",5e3),console.log("nanyuan "+e))}))}}}),d=n(22),component=Object(d.a)(c,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("section",[n("p",{staticClass:"title m-5 pt-5"},[t._v("RFID-tagged tray-returns data")]),t._v(" "),n("div"),t._v(" "),n("div",{staticClass:"columns mt-5 is-multiline is-tablet"},[n("div",{staticClass:"column is-4 has-text-centered"},[n("div",{staticClass:"card"},[n("div",{staticClass:"card-content"},[n("p",{staticClass:"title is-size-5-touch"},[t._v("Daily Tray Return Count")]),t._v(" "),n("b-field",{attrs:{label:"Select a date"}},[n("b-datepicker",{attrs:{placeholder:"Click to select...","min-date":t.minDate,"max-date":t.maxDate},model:{value:t.date,callback:function(e){t.date=e},expression:"date"}})],1),t._v(" "),n("line-chart",{ref:"nanyuanLineChart",attrs:{chartData:this.cleanerReturnInsights}})],1)])]),t._v(" "),n("div",{staticClass:"column is-4 has-text-centered"},[n("div",{staticClass:"card"},[n("div",{staticClass:"card-content"},[n("p",{staticClass:"title is-size-5-touch"},[t._v("Tray Return Visualisation")]),t._v(" "),n("pie-chart",{ref:"nanyuanPieChart",attrs:{chartData:this.nanyuanReturns}})],1)])]),t._v(" "),n("div",{staticClass:"column is-4 has-text-centered"},[n("div",{staticClass:"card"},[n("div",{staticClass:"card-content"},[n("p",{staticClass:"title is-size-5-touch"},[t._v("Tray Return Rate")]),t._v(" "),n("card-widget",{staticClass:"tile is-child",attrs:{type:"is-success",icon:"charity",number:this.selfReturn,suffix:"%",label:"Self-returns rate",description:"Percentage of patrons who cleaned up their tables after eating today"}}),t._v(" "),n("card-widget",{staticClass:"tile is-child",attrs:{type:"is-danger",icon:"account-multiple-minus",number:this.cleanerReturn,suffix:"%",label:"Cleaner Return rate",description:"Percentage of patrons who left their receptacles to the cleaners today"}})],1)])])])])}),[],!1,null,null,null);e.default=component.exports;installComponents(component,{LineChart:n(223).default,PieChart:n(224).default,CardWidget:n(222).default})}}]);