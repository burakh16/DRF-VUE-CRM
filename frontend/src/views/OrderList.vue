<template>
  <div>
    <Table
      :headers="headers"
      :items="getOrders.data"
      :pagination="getOrders.pagination"
      title="Order"
      @new_item="newOrder"
      @edit_item="editOrder"
      @change_page="onPageChange"
    >
    </Table>
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
        { text: "Customer", value: "customer" },
        { text: "Order Date", value: "order_date" },
        { text: "Actions", value: "actions", sortable: false }
      ]
    };
  },
  components: {
    Table
  },
  methods: {
    ...mapActions(["get_orders"]),
    newOrder() {
      this.$router.push("/order");
    },
    editOrder(id) {
      this.$router.push(`/order/${id}`);
    },
    onPageChange(page) {
      this.get_orders(page);
    }
  },
  computed: {
    ...mapGetters(["getOrders"])
  },
  created() {
    this.get_orders();
  }
};
</script>

<style>
</style>