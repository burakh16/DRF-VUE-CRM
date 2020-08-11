<template>
  <v-app>
     <vue-confirm-dialog></vue-confirm-dialog>
    <v-app-bar app color="primary" dark dense fixed>
      <div class="d-flex align-center">CRM</div>

      <v-spacer></v-spacer>

      <v-btn href="https://github.com/vuetifyjs/vuetify/releases/latest" target="_blank" text>
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-container fluid class="mt-5 h-100">
      <v-row>
        <v-col cols="2">
          <Sidebar />
        </v-col>

        <v-col cols="8" class="mt-5">
          <router-view></router-view>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import Sidebar from "@/components/Sidebar.vue";

export default {
  name: "App",
  data: () => ({
    //
  }),
  components: {
    Sidebar
  }
};
</script>

<style>
.h-100 {
  height: 100%;
}
</style>