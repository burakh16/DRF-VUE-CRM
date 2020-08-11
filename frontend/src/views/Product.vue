<template>
  <v-card outlined>
    <v-card-title>
      <v-row>
        <v-col cols="8">Product</v-col>
      </v-row>
    </v-card-title>
    <v-card-text>
      <v-form ref="form" lazy-validation v-model="valid" @submit.prevent="save">
        <v-row>
          <v-col cols="5">
            <v-text-field outlined v-model="product.code" :rules="nameRules" label="Code" required></v-text-field>
          </v-col>
          <v-col cols="7">
            <v-text-field outlined v-model="product.name" :rules="nameRules" label="Name" required></v-text-field>
          </v-col>
          <v-col cols="5">
            <v-text-field
              outlined
              v-model="product.qty"
              :rules="nameRules"
              label="Quantity"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="7">
            <v-text-field
              outlined
              v-model="product.price"
              :rules="nameRules"
              label="Price"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field
              outlined
              v-model="product.description"
              :rules="nameRules"
              label="Description"
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
              v-if="product.id !== 0"
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
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      product: {
        id: 0,
        code: "",
        name: "",
        descripton: "",
        qty: "",
        price: ""
      },
      nameRules: [v => !!v || "This field is required"],
      valid: true,
      state: false
    };
  },
  methods: {
    ...mapActions([
      "add_product",
      "update_product",
      "get_product",
      "delete_product"
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
            if (this.product.id === 0) {
              this.add_product(this.product);
              this.$toast.success("Product Created!");
            } else {
              console.log(this.product)
              this.update_product(this.product);
              this.$toast.success("Product Update!");
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
            this.delete_product(this.product.id);
            this.$router.push("/products");
            this.$toast.success("Product Deleted!");
          }
        }
      });
    }
  },
  computed: {
    ...mapGetters(["getProduct"])
  },
  created() {
    const id = this.$route.params.id;
    if (id !== undefined)
      this.get_product(id).then(() => (this.product = this.getProduct));
  }
};
</script>

<style>
</style>