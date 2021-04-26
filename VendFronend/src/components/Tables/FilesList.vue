<template>
  <div>
    
    <md-table v-model="users" :table-header-color="tableHeaderColor">
      
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label=""><input type="checkbox" :id="item.ID" :value="item.FileName" v-model="selectedV"></md-table-cell>
        <md-table-cell md-label="ID">{{ item.ID }}</md-table-cell>
        <md-table-cell md-label="File Name">{{ item.FileName }}</md-table-cell>
        <md-table-cell md-label="File Type">{{ item.FileType }}</md-table-cell>
        
        <!-- <md-table-cell md-label="Total Money OUT 30 Days">{{ item.TMOUT30 }}</md-table-cell>
        <md-table-cell md-label="Total Money IN Daily">{{ item.TMIND }}</md-table-cell>
        <md-table-cell md-label="Total Money OUT Daily">{{ item.TMOUTD }}</md-table-cell> -->
      </md-table-row>
    </md-table>
  </div>
</template>

<script>

//import selected from '@/assets/js/helper.js'
export default {
  name: "FilesList",
  props: {
    tableHeaderColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      selectedV: [],
      allData:this.$store.state.filesData,
      users: [
       
      ]
    };
  },
methods:{

getData(){
// fetch(API_URL)
//       .then(response => response.json())
//       .then(result => {
        
        
//         this.allData = result['data']
//         this.users=this.allData
//         //console.clear()
        
//       //  console.log(this.allData)
//         //JSON.parse(result['data'])

//       });
//this.allData=[]
//this.getFilesList();
this.allData=this.$store.state.filesData
this.users=this.allData;
//selected=this.selectedV;
//this.$SelectedV=this.selectedV
this.$store.state.selectedCheckBoxes=this.selectedV;
// console.log('selectedV',this.selectedV)
// console.log('selectedSTORE;',this.$store.state.totalTvCount)
  },
},

  mounted(){
    this.getData()
    
    this.$nextTick(function () {
            window.setInterval(() => {
                this.getData();
                // this.allData=this.$store.state.filesData
                // this.users=this.allData;
            },200);
        })
    this.getData()
  }
};
</script>
