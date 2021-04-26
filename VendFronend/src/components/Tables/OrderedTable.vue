<template>
  <div>
    <md-table v-model="users" :table-header-color="tableHeaderColor">
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID">{{ item.ID }}</md-table-cell>
        <md-table-cell md-label="Time Stamp">{{ item.Timestamp }}</md-table-cell>
        <md-table-cell md-label="File Name">{{ item.FileName }}</md-table-cell>
        <md-table-cell md-label="Job Type">{{ item.JobType }}</md-table-cell>
        <md-table-cell md-label="Credits Used">{{ item.CreditsUsed }}</md-table-cell>
        <md-table-cell md-label="Reward Points Earned">{{ item.RewardPointsEarned }}</md-table-cell>
        
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
const API_URL_USERLedger = "http://bkc-backend.production.wrapdrive.tech/v1/getUserLedger";
export default {
  name: "ordered-table",
  props: {
    tableHeaderColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      selected: [],
      allData:[],
      users: [
        {
          id: 1,
          name: "D1akota Rice",
          salary: "$36,738",
          country: "Niger",
          city: "Oud-Turnhout"
        },
        {
          id: 2,
          name: "Minerva Hooper",
          salary: "$23,738",
          country: "Curaçao",
          city: "Sinaai-Waas"
        },
        {
          id: 3,
          name: "Sage Rodriguez",
          salary: "$56,142",
          country: "Netherlands",
          city: "Overland Park"
        },
        {
          id: 4,
          name: "Philip Chaney",
          salary: "$38,735",
          country: "Korea, South",
          city: "Gloucester"
        }
      ]
    };
  },

  
methods:{
getData(){
const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email: this.$store.state.loggedInUserDetails['Email'] })
  };
  fetch(API_URL_USERLedger, requestOptions)
    .then(response => response.json())
    .then(result => {
        
        // console.log(result.data)
        this.allData = result['data']

        this.users=this.allData
        this.$store.state.loggedInUserDetails['TotalJobs']=this.users.length
        // console.log(this.users)
        });
  },
},
  mounted(){
    this.$nextTick(function () {
            window.setInterval(() => {
                this.getData();
            },2000);
        })
    // this.getData()
  }
};
</script>
