<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item">
        <md-card>
          <md-card-header data-background-color="purple">
            <h4 class="title">Controller</h4>
            <p class="category">
              Interact with your Backup-Computer
            </p>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100">
                   <div
                 class="md-layout-item md-medium-size-100 md-xsmall-size-150 md-size-150"
          >
                    <md-card>
                      <md-card-header data-background-color="blue">
                        <h4 class="title">Controller</h4>
                        <p class="category">Select the function(s) below to start a job</p>
                      </md-card-header>
                      <md-card-content  >
                        
                        <md-button class="md-primary md-lg" @click="copy()"><md-icon >file_copy</md-icon>Copy</md-button>
                        <div class="md-layout-item md-small-size-100 md-size-50">
                        <md-field>
                          <label>Number of Copies</label>
                          <md-input v-model="noOfCopies" type="number"></md-input>
                        </md-field>
                      </div>
                        <md-button class="md-primary md-lg" @click="print()"><md-icon >print</md-icon>Print</md-button>
                        <md-button class="md-primary md-lg" @click="scan()"><md-icon >document_scanner</md-icon>Scan</md-button>
                        <md-button class="md-primary md-lg" @click="fax()"><md-icon >receipt_long</md-icon>Fax</md-button>
                      </md-card-content>
                    </md-card>
                  </div>
                  <!-- <h5>Control Center</h5>
                <div class="alert alert-info">
                  <span>This is a plain notification</span>
                </div>
                <div class="alert alert-info">
                  <button type="button" aria-hidden="true" class="close">
                    ×
                  </button>
                  <span>This is a notification with close button.</span>
                </div>
                <div
                  class="alert alert-info alert-with-icon"
                  data-notify="container"
                >
                  <button type="button" aria-hidden="true" class="close">
                    ×
                  </button>
                  <i data-notify="icon" class="material-icons">add_alert</i>
                  <span data-notify="message"
                    >This is a notification with close button and icon.</span
                  >
                </div> -->
                <!-- <div
                  class="alert alert-info alert-with-icon"
                  data-notify="container"
                >
                  <button type="button" aria-hidden="true" class="close">
                    ×
                  </button>
                  <i data-notify="icon" class="material-icons">add_alert</i>
                  <span data-notify="message"
                    >This is a notification with close button and icon and have
                    many lines. You can see that the icon and the close button
                    are always vertically aligned. This is a beautiful
                    notification. So you don't have to worry about the
                    style.</span
                  >
                </div> -->
              </div>
              <div class="md-layout-item md-medium-size-100">
                <div
        class="md-layout-item md-medium-size-100 md-xsmall-size-150 md-size-150"
      >
      <md-button class="md-primary" @click="refreshFilesList()">
                   Refresh List 
        </md-button>
        <md-card>
        
        
          <md-card-header data-background-color="green">
            <h4 class="title">Files</h4>
            <p class="category">Files List</p>
          </md-card-header>
          <md-card-content  >
            <FilesList  table-header-color="blue"></FilesList>
          </md-card-content>
        </md-card>
        
        
        
        
      </div>




                
                <!-- <div class="alert alert-info">
                  <button type="button" aria-hidden="true" class="close">
                    ×
                  </button>
                  <span
                    ><b> Info - </b> This is a regular notification made with
                    ".alert-info"</span
                  >
                </div>
                <div class="alert alert-success">
                  <button type="button" aria-hidden="true" class="close">
                    ×
                  </button>
                  <span
                    ><b> Success - </b> This is a regular notification made with
                    ".alert-success"</span
                  >
                </div>
                <div class="alert alert-warning">
                  <button type="button" aria-hidden="true" class="close">
                    ×
                  </button>
                  <span
                    ><b> Warning - </b> This is a regular notification made with
                    ".alert-warning"</span
                  >
                </div>
                <div class="alert alert-danger">
                  <button type="button" aria-hidden="true" class="close">
                    ×
                  </button>
                  <span
                    ><b> Danger - </b> This is a regular notification made with
                    ".alert-danger"</span
                  >
                </div>
                <div class="alert alert-primary">
                  <button type="button" aria-hidden="true" class="close">
                    ×
                  </button>
                  <span
                    ><b> Primary - </b> This is a regular notification made with
                    ".alert-primary"</span
                  >
                </div>
              </div>

              <div class="md-layout-item md-size-100">
                <div class="places-buttons text-center">
                  <h5 class="text-center">
                    Notifications Places
                    <p class="category">Click to view notifications</p>
                  </h5>
                  <md-button
                    class="md-primary"
                    @click="notifyVue('top', 'left')"
                    >Top Left</md-button
                  >
                  <md-button
                    class="md-primary"
                    @click="notifyVue('top', 'center')"
                    >Top Center</md-button
                  >
                  <md-button
                    class="md-primary"
                    @click="notifyVue('top', 'right')"
                    >Top Right</md-button
                  >
                  <md-button
                    class="md-primary"
                    @click="notifyVue('bottom', 'left')"
                    >Bottom Left</md-button
                  >
                  <md-button
                    class="md-primary"
                    @click="notifyVue('bottom', 'center')"
                    >Bottom Center</md-button
                  >
                  <md-button
                    class="md-primary"
                    @click="notifyVue('bottom', 'right')"
                    >Bottom Right</md-button
                  >
                </div> -->
              </div>
            </div>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>
const API_URL_RewardsCredsUpdate = "http://bkc-backend.production.wrapdrive.tech/v1/rewardCredsUpdate";
const API_URL_LedgerUpdate = "http://bkc-backend.production.wrapdrive.tech/v1/ledgerUpdate";
const API_URL_FILESLIST = "http://bkc-backend.production.wrapdrive.tech/v1/filesList";

import {
  
  
  
  FilesList
} from "@/components";

export default {
  props: {
  imgLogo: {
      type: String,
      default: require("@/assets/img/vue-logo.png")
    },
  },
  components: {
    
    // ChartCard,
    
    FilesList
  },
  data() {
    return {
      file:'',
      noOfCopies:1,
      allData:[],
      type: ["", "info", "success", "warning", "danger"],
      notifications: {
        topCenter: false
      }
    };
  },
  
  methods: {
    getFilesList(){
const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email: this.$store.state.loggedInUserDetails['Email'] })
  };
  fetch(API_URL_FILESLIST, requestOptions)
    .then(response => response.json())
    .then(result => {
        
       
        });
  },

    refreshFilesList(){
      
      this.allData=[];
      this.$store.state.filesData=[];
      this.getFilesList();
    //this.file = this.$refs.file.files[0];
    //console.log(this.file)
  },

    notifyVue(verticalAlign, horizontalAlign,clr) {
      var color = Math.floor(Math.random() * 4 + 1);
      this.$notify({
        message:
          "Welcome to <b>Material Dashboard</b> - a beautiful freebie for every web developer.",
        icon: "add_alert",
        horizontalAlign: horizontalAlign,
        verticalAlign: verticalAlign,
        type: this.type[color]
      });
    },

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
    appendLedger(type){
      var itemsList=this.$store.state.selectedCheckBoxes;
      var revPtsEarned=itemsList.length;
      var credPtsUsed=itemsList.length;
      var FilName=itemsList.toString();
      
      var jobType="";
      
      if(type=="p"){
          jobType="Print"
          revPtsEarned=itemsList.length*0.5;
          credPtsUsed=itemsList.length*1
      }

      if(type=="c"){
          jobType="Copy"
          revPtsEarned=this.noOfCopies*0.2;
          credPtsUsed=this.noOfCopies*0.4;
          FilName="N/A"
      }
      if(type=="s"){
          jobType="Scan"
          revPtsEarned=0.2;
          credPtsUsed=0.2;
          FilName="N/A";
      }
    if(type=="f"){
          jobType="Fax"
          revPtsEarned=itemsList.length*0.65;
          credPtsUsed=itemsList.length*1.2
      }

      
    const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ 
                            FileName:FilName,
                            JobType:jobType,
                            CreditsUsed:String(credPtsUsed),
                            RewardPointsEarned: String(revPtsEarned),
                            
                            
                           Email: this.$store.state.loggedInUserDetails['Email'] 
    })
  };
  fetch(API_URL_LedgerUpdate, requestOptions)
    .then(response => response.json())
    .then(

    );
    },
    initiateJob(type){
      var revPts=parseInt(this.$store.state.loggedInUserDetails['RewardPoints']);
      var credPts=parseInt(this.$store.state.loggedInUserDetails['Credits']);
      var itemsList=this.$store.state.selectedCheckBoxes;
      if(type=="p"){
        revPts=revPts+0.5*itemsList.length;
        credPts=credPts-itemsList.length;
          
      }
      if(type=="c"){
        revPts=revPts+0.2*this.noOfCopies;
        credPts=credPts-this.noOfCopies*0.4;
      }
      if(type=="s"){
        revPts=revPts+0.2*1;
        credPts=credPts-(1*0.2);
      }
      if(type=="f"){
        revPts=revPts+0.65*itemsList.length;
        credPts=credPts-itemsList.length*1.2;
      }
      
    const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ RewardPoints: String(revPts),
                            Credits:String(credPts),
                           Email: this.$store.state.loggedInUserDetails['Email'],
                           JobType: type,
    })
  };
  fetch(API_URL_RewardsCredsUpdate, requestOptions)
    .then(response => response.json())
    .then(
      this.$store.state.loggedInUserDetails['Credits']=credPts,
      this.$store.state.loggedInUserDetails['RewardPoints']=revPts,
      
      this.appendLedger(type)
      

      //this.notifyM("top","right",2,'Redeemed','Rewards Redeemed.')

    );//data => (this.postId = data.id)
      
  },
    print(){
      var itemsList=this.$store.state.selectedCheckBoxes;
      
      if(itemsList.length==0){
        console.log(itemsList)
          this.notifyM("top","right",4,'Error','Please select file(s) to print.')
      }
      else{
          console.log(itemsList)
        console.log('printing')
        this.initiateJob("p");
        
        this.notifyM("top","right",2,'Printing','Print job added successfully.')
      }
    },
    copy(){
      this.initiateJob("c");
        
        this.notifyM("top","right",2,'Copying','Copy job added successfully.')
      // console.log(this.$store.state.loggedInUser)
      // console.log(this.$store.state.loggedInUserDetails['FName'])

    },
    scan(){
      this.initiateJob("s");
        
        this.notifyM("top","right",2,'Scanning','Scan job added successfully.')
      // console.log(this.$store.state.loggedInUser)
      // console.log(this.$store.state.loggedInUserDetails['FName'])

    },
    fax(){
      var itemsList=this.$store.state.selectedCheckBoxes;
       if(itemsList.length==0){
         console.log(itemsList)
          this.notifyM("top","right",4,'Error','Please select file(s) to fax.')
      }
      else{
      this.initiateJob("f");
        
        this.notifyM("top","right",2,'Fax','Fax job added successfully.')
      }
      // console.log(this.$store.state.loggedInUser)
      // console.log(this.$store.state.loggedInUserDetails['FName'])

    }
  },
  mounted(){
    this.getFilesList();
  }
};
</script>
