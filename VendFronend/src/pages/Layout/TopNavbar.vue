<template>
  <md-toolbar md-elevation="0" class="md-transparent" v-if="$route.meta.showSidebar">
    <div class="md-toolbar-row">
      <div class="md-toolbar-section-start">
        <h3 class="md-title">{{ $route.name }}</h3>
      </div>
      <div class="md-toolbar-section-end">
        <md-button
          class="md-just-icon md-simple md-toolbar-toggle"
          :class="{ toggled: $sidebar.showSidebar }"
          @click="toggleSidebar"
        >
          <!-- <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span> -->
        </md-button>

        <div class="md-collapse">
           
          <md-list>
           
            <li class="md-list-item">
            
                <div class="md-list-item-content">
                  <drop-down>
                  
                    <ul class="dropdown-menu dropdown-menu-right">
                     
                    </ul>
                  </drop-down>
                </div>
              
            </li>

              <li class="md-list-item">
              <a class="md-list-item-router md-list-item-container dropdown">
                <div class="md-list-item-content">
                  <drop-down>
               
                    <ul class="dropdown-menu dropdown-menu-right">
                   
                    </ul>
                  </drop-down>
                </div>
              </a>
            </li>

            
          </md-list>
        </div>
      </div>
    </div>
  </md-toolbar>
</template>

<script>
export default {
  data() {
    return {
      timestamp:"",
      selectedEmployee: null,
      employees: [
        "Jim Halpert",
        "Dwight Schrute",
        "Michael Scott",
        "Pam Beesly",
        "Angela Martin",
        "Kelly Kapoor",
        "Ryan Howard",
        "Kevin Malone"
      ]
    };
  },
  created() {
                setInterval(this.getNow, 1000);
            },
  methods: {
    toggleSidebar() {
      this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
    },
    getNow: function() {
                    const today = new Date();
                    const date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
                    const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
                    const dateTime = date +' '+ time;
                    this.timestamp = dateTime;
                }
  }
};
</script>

<style lang="css"></style>
