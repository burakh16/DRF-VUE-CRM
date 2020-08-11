<template>
  <div>
    <v-card outlined>
      <v-card-title class="py-0">
        <v-row>
          <v-col cols="12">
            Order
            <v-divider class="my-1"></v-divider>
          </v-col>
        </v-row>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" lazy-validation v-model="valid" @submit.prevent="save">
          <v-row>
            <v-col cols="6">
              <v-autocomplete v-model="order.customer" label="Customer" :items="customers" outlined></v-autocomplete>
            </v-col>
            <v-col cols="6">
              <v-text-field
                outlined
                v-model="order.order_date"
                :rules="nameRules"
                label="Cell"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                outlined
                v-model="order.shipping_date"
                :rules="nameRules"
                label="District"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                outlined
                v-model="order.description"
                :rules="nameRules"
                label="City"
                required
              ></v-text-field>
            </v-col>

            <v-col cols="12">
              <v-btn
                outlined
                color="blue-grey"
                type="submit"
                class="float-right"
                :disabled="!valid"
              >Save</v-btn>
              <v-btn
                v-if="order.id !== 0"
                outlined
                color="red"
                type="button"
                class="float-right mr-3"
                :disabled="!valid"
                :hidden="!state"
                @click="onDelete"
              >Delete</v-btn>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>
    <Table
    class="mt-5"
      :headers="headers"
      :items="order.items"
      title="Items"
      @change_page="onPageChange"
      @selected="onProductSelect"
      @new_item="addItem"
    />
    <!-- Modal -->
    <v-dialog v-model="dialog" max-width="1000">
      <Table
        :headers="product_headers"
        :items="getProducts.data"
        :pagination="getProducts.pagination"
        title="Please select a product!"
        @change_page="onPageChange"
        @selected="onProductSelect"
        :edit="edit"
      />
    </v-dialog>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

import Table from "@/components/Table";

export default {
  data() {
    return {
      order: {
        id: 0,
        customer: "",
        order_date: "",
        shipping_date: "",
        description: "",
        items: []
      },
      item: {
        product_id: Number,
        product_name: String,
        qty: Number,
        price: Number,
        total: Number
      },
      edit: false,
      product_headers: [
        { text: "#", value: "id" },
        { text: "Product Code", value: "code" },
        { text: "Product Name", value: "name" },
        { text: "Description", value: "description" },
        { text: "Price ($)", value: "price" },
        { text: "Quantity", value: "qty" },
        { text: "Actions", value: "actions", sortable: false }
      ],
      headers: [
        { text: "#", value: "id" },
        { text: "Product ", value: "product_name" },
        { text: "Quantity", value: "qty" },
        { text: "Price ($)", value: "price" },
        { text: "Actions", value: "actions", sortable: false }
      ],
      customers: [],
      nameRules: [v => !!v || "This field is required"],
      valid: true,
      state: false,
      dialog: false
    };
  },
  components: {
    Table
  },
  methods: {
    ...mapActions([
      "add_order",
      "update_order",
      "get_order",
      "delete_order",
      "get_customers_without_pages",
      "get_available_products"
    ]),
    save() {
      this.$confirm({
        message: `Are you sure?`,
        button: {
          no: "No",
          yes: "Yes"
        },
        callback: confirm => {
          if (confirm) {
            if (this.order.id === 0) {
              this.add_order(this.order);
              this.$toast.success("Order Created!");
            } else {
              this.update_order(this.order);
              this.$toast.success("Order Update!");
            }
          }
        }
      });
    },
    onDelete() {
      this.$confirm({
        message: `Are you sure?`,
        button: {
          no: "No",
          yes: "Yes"
        },
        callback: confirm => {
          if (confirm) {
            this.delete_order(this.order.id);
            this.$router.push("/orders");
            this.$toast.success("Order Deleted!");
          }
        }
      });
    },
    onPageChange(page) {
      this.get_available_products(page);
    },
    onProductSelect(product) {
      this.dialog = false;
      this.item = {
        product_id: product.id,
        product_name: product.name,
        price: product.price,
        total: product.price
      };
      this.order.items.push(this.item);
    },
    addItem(){
      this.dialog = true;
    }
  },
  computed: {
    ...mapGetters(["getOrder", "getCustomers", "getProducts"])
  },
  created() {
    const id = this.$route.params.id;
    if (id !== undefined)
      this.get_order(id).then(() => (this.order = this.getOrder));
    this.get_customers_without_pages().then(() => {
      this.customers = this.getCustomers.map(customer => {
        return {
          text: customer.name,
          value: customer.id
        };
      });
    });
    this.get_available_products();
  }
};
</script>

<style>
</style>