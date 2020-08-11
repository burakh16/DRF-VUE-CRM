<template>
  <div>
    <Table
      :headers="headers"
      :items="getCustomers.data"
      :pagination="getCustomers.pagination"
      title="Customers"
      @new_item="newCustomer"
      @edit_item="editCustomer"
      @change_page="onPageChange"
    />    
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

import Table from "@/components/Table.vue";

export default {
  data() {
    return {
      headers: [
        { text: "#", value: "id" },
        { text: "Name", value: "name" },
        { text: "City", value: "city" },
        { text: "Cell Number", value: "cell_number" },
        { text: "Actions", value: "actions", sortable: false }
      ]
    };
  },
  components: {
    Table
  },
  methods: {
    ...mapActions(["get_customers"]),
    newCustomer() {
      this.$router.push("/customer");
    },
    editCustomer(id) {
      this.$router.push(`/customer/${id}`);
    },
    onPageChange(page) {
      this.get_customers(page);
    }
  },
  computed: {
    ...mapGetters(["getCustomers"])
  },
  created() {
    this.get_customers();
  }
};
</script>

<style>
</style>