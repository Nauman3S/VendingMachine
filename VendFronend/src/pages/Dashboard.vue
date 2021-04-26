<template>
  <div class="content">
    <div class="md-layout">
    
      

      <div class="md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-35">
        
        <stats-card data-background-color="orange">
          <template slot="header">
            <md-icon>update</md-icon>
          </template>

          <template slot="content">
            <p class="category">Next Vend Time</p>
            <h4 class="title">{{nextVendAt}}</h4>
          </template>
          

            <!-- <template slot="footer">
              <div class="stats">
                <md-icon>date_range</md-icon>
                Last 30 Days
              </div>
            </template> -->
        </stats-card>
        <md-button class="md-primary md-round md-lg btn-just-icon" @click="vend()"><md-icon >precision_manufacturing</md-icon>Vend</md-button>
        
      </div>

      
      <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-150 md-size-150"
      >
        <md-card>
          
          
        </md-card>
      </div>
      
    </div>
  </div>
</template>

<script>
const API_URL_Verify = "http://vend-backend.production.wrapdrive.tech/v1/verifyFingerPrint";
const API_URL_NEWFP = "http://vend-backend.production.wrapdrive.tech/v1/newFingerPrint";
const API_URL_RetVend = "http://vend-backend.production.wrapdrive.tech/v1/vend";

import FingerprintJS from '@fingerprintjs/fingerprintjs'
import {
  StatsCard,
  ChartCard,
  
  
  OrderedTable
} from "@/components";

export default {
  components: {
    StatsCard,
    // ChartCard,
    
  },
  data() {
    return {
       
      dataD:'asd',
      Fingerprint:"",
      nextVendAt:'Click Vend to Reveal',
      
      Timestamp:'',
      FileName:'',
      JobType:'',
      CreditsUsed:'',
      RewardPointsEarned:'',
      dailySalesChart: {
        data: {
          labels: ["M", "T", "W", "T", "F", "S", "S"],
          series: [[12, 17, 7, 17, 23, 18, 38]]
        },
        options: {
          lineSmooth: this.$Chartist.Interpolation.cardinal({
            tension: 0
          }),
          low: 0,
          high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0
          }
        },
        
      },
      dataCompletedTasksChart: {
        data: {
          labels: ["12am", "3pm", "6pm", "9pm", "12pm", "3am", "6am", "9am"],
          series: [[230, 750, 450, 300, 280, 240, 200, 190]]
        },

        options: {
          lineSmooth: this.$Chartist.Interpolation.cardinal({
            tension: 0
          }),
          low: 0,
          high: 1000, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0
          }
        }
      },
      emailsSubscriptionChart: {
        data: {
          labels: [
            "Ja",
            "Fe",
            "Ma",
            "Ap",
            "Mai",
            "Ju",
            "Jul",
            "Au",
            "Se",
            "Oc",
            "No",
            "De"
          ],
          series: [[542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895]]
        },
        options: {
          axisX: {
            showGrid: false
          },
          low: 0,
          high: 1000,
          chartPadding: {
            top: 0,
            right: 5,
            bottom: 0,
            left: 0
          }
        },
        responsiveOptions: [
          [
            "screen and (max-width: 640px)",
            {
              seriesBarDistance: 5,
              axisX: {
                labelInterpolationFnc: function(value) {
                  return value[0];
                }
              }
            }
          ]
        ]
      }
    };
  },
  methods:{
    newFPVend(){
      const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ Fingerprint: this.Fingerprint, LastVend:this.Timestamp })
  };
      fetch(API_URL_NEWFP, requestOptions)
    .then(response => response.json())
    .then(result => {
      console.log(result)
      
        
       
        });

    },
    returningVend(){
      const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ Fingerprint: this.Fingerprint, LastVend:this.Timestamp })
  };
      fetch(API_URL_RetVend, requestOptions)
    .then(response => response.json())
    .then(result => {
      console.log(result)
      
        
       
        });

    },
    get24HDiff(now){
       var n=new Date(new Date(now).getTime() + 60 * 60 * 24 * 1000);
       console.log(n)
       return n
       
    },
    getNow() {
                    const today = new Date();
                    // const date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
                    // const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
                    // const dateTime = date +' '+ time;
                    this.Timestamp = today;
                    return today;
                },
    
    vend(){
      this.getNow();
      console.log(this.Timestamp)
      this.get24HDiff(this.Timestamp);
      console.log(this.getNow().getTime()>this.get24HDiff(this.Timestamp).getTime())
        
     
     

          if(this.Fingerprint!=""){
            console.log(this.Fingerprint)

            const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ Fingerprint: this.Fingerprint })
  };
      fetch(API_URL_Verify, requestOptions)
    .then(response => response.json())
    .then(result => {
      console.log(result)
      if(result['data'].length==0){
        console.log('empty, creating new fp')
        this.newFPVend();
      }
      else{
        var lv=result['data'][0]['LastVend'];
        console.log()
        this.nextVendAt=this.get24HDiff(lv)
        console.log('updating fp')
        //this.returningVend();
        if(this.getNow().getTime()>=this.nextVendAt.getTime){
        this.returningVend();
        }

      }
        
       
        });
          }
    },
getData(){
  

  },
},
  mounted(){
  const fpPromise = FingerprintJS.load()
    ;(async () => {
  // Get the visitor identifier when you need it.
  const fp = await fpPromise
  const result = await fp.get()

  // This is the visitor identifier:
  const visitorId = result.visitorId
  console.log(visitorId)
  this.Fingerprint=visitorId
    })()
    // this.$nextTick(function () {
    //         window.setInterval(() => {
    //             this.getData();
    //         },2000);
    //     })
  //  / this.getData()
  }
};
</script>
