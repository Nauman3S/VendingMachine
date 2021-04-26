<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <edit-profile-form data-background-color="green"> </edit-profile-form>
      </div>
      <div class="md-layout-item md-medium-size-100 md-size-33">
        <user-card> </user-card>
        
      </div>
       <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-33 md-size-66"
      >
        <md-card>
          <md-card-header data-background-color="teal">
            <h4 class="title">Credits</h4>
            <p class="category">Credits Management</p>
          </md-card-header>
          <md-card-content  >
            <h4>Credits: ${{this.$store.state.loggedInUserDetails['Credits']}}</h4>
            <h4>Reward Points: {{this.$store.state.loggedInUserDetails['RewardPoints']}}</h4>
            <h4>{{this.$store.state.rewardToCreds}} Reward Point = ${{rewardToCredit}} Credit</h4>

            <input type="text" name="username" placeholder="Credits value" v-model="reqCredits"  /><br>
            <md-button class="md-raised md-primary" @click="reqCdts()">
                   Request Credits
        </md-button>

        <md-button class="md-raised md-primary" @click="redeem()">
                   Redeem Reward Points
        </md-button>
          </md-card-content>
        </md-card>
        
        
        
      </div>
      
    </div>
  </div>
</template>

<script>
const API_URL_Creds = "http://bkc-backend.production.wrapdrive.tech/v1/credReq";
const API_URL_R_Creds = "http://bkc-backend.production.wrapdrive.tech/v1/rewardToCred";

import { EditProfileForm, UserCard } from "@/pages";

export default {
  components: {
    EditProfileForm,
    UserCard
  },
    data() {
    return {
      type: ["", "info", "success", "warning", "danger"],
      notifications: {
        topCenter: false
      },
      credits: "21",
      rewards: "5",
      reqCredits: "",
      rewardToCredit: "1",
       
     
      }
    
  },

    methods:{
       notifyM(verticalAlign, horizontalAlign,clr,title,msg) {
      var color = clr;//Math.floor(Math.random() * 4 + 1);
      this.$notify({
        message:
          "<b>"+title+"</b><br>"+msg,
        icon: "add_alert",
        horizontalAlign: horizontalAlign,
        verticalAlign: verticalAlign,
        type: this.type[color]
      });
    },

  CreditsReqF(){
     const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ CreditsRequest: this.reqCredits, Email: this.$store.state.loggedInUserDetails['Email'] 
    })
  };
  fetch(API_URL_Creds, requestOptions)
    .then(response => response.json())
    .then(
      
      
    );//data => (this.postId = data.id)


  },
    reqCdts(){
        console.log(this.reqCredits)
        if(this.reqCredits!=""){
          if(!isNaN(this.reqCredits)){
              this.notifyM("top","right",2,'Credits Request','Credits request made.')
              this.CreditsReqF()
          }
          
        }
        else{
            this.notifyM("top","right",4,'Error','Please enter a valid amount.')
        }
    },
    calcCreds(){
      var g=parseInt (this.$store.state.loggedInUserDetails['RewardPoints'])
      if(g!=0){
      var m=g/parseInt(this.$store.state.rewardToCreds)

      var cr=parseInt(this.$store.state.loggedInUserDetails['Credits'])

      var res=String(cr+m)
      return res;
      }
      else{
        return "0";
      }
    },
    redeem(){
      if(this.calcCreds()!="0"){
       const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ RewardPoints: "0",
                            Credits:this.calcCreds(),
                           Email: this.$store.state.loggedInUserDetails['Email'] 
    })
  };
  fetch(API_URL_R_Creds, requestOptions)
    .then(response => response.json())
    .then(
      this.$store.state.loggedInUserDetails['Credits']=this.calcCreds(),
      this.credits=this.calcCreds(),
      this.$store.state.loggedInUserDetails['RewardPoints']="0",
      this.rewards="0",

      this.notifyM("top","right",2,'Redeemed','Rewards Redeemed.')

    );//data => (this.postId = data.id)
      }
  },

    
    }
};
</script>
