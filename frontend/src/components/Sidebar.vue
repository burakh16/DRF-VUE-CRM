<template>
  <v-navigation-drawer permanent class="h-100">
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="title">Application</v-list-item-title>
        <v-list-item-subtitle>subtext</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-divider></v-divider>

    <v-list dense nav>
      <v-list-item v-for="item in items" :key="item.title" link :to="item.slug">
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { title: "Dashboard", icon: "mdi-view-dashboard", slug: "/" },
        { title: "Order", icon: "mdi-image", slug: "/orders" },
        { title: "Customer", icon: "mdi-help-box", slug: "/customers" },
        { title: "Product", icon: "mdi-help-box", slug: "/products" }
      ]
    };
  }
};
</script>

<style>
</style>