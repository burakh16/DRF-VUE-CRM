<template>
  <div>
    <Table
      :headers="headers"
      :items="getProducts.data"
      :pagination="getProducts.pagination"
      title="Products"
      @new_item="newProduct"
      @edit_item="editProduct"
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
        { text: "Product Code", value: "code" },
        { text: "Product Name", value: "name" },
        { text: "Description", value: "description" },
        { text: "Price ($)", value: "price" },
        { text: "Quantity", value: "qty" },
        { text: "Actions", value: "actions", sortable: false }
      ]
    };
  },
  components: {
    Table
  },
  methods: {
    ...mapActions(["get_products"]),
    newProduct() {
      this.$router.push("/product");
    },
    editProduct(id) {
      this.$router.push(`/product/${id}`);
    },
    onPageChange(page) {
      this.get_products(page);
    },
    
  },
  computed: {
    ...mapGetters(["getProducts"])
  },
  created() {
    this.get_products();
  }
};
</script>

<style>
</style>