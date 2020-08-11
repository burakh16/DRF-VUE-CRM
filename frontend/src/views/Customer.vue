<template>
  <v-card outlined>
    <v-card-title class="pb-0">
      <v-row>
        <v-col cols="12">
          Customer
          <v-divider class="my1"></v-divider>
        </v-col>
      </v-row>
    </v-card-title>
    <v-card-text>
      <v-form ref="form" lazy-validation v-model="valid" @submit.prevent="save">
        <v-row>
          <v-col cols="6">
            <v-text-field outlined v-model="customer.name" :rules="nameRules" label="Name" required></v-text-field>
          </v-col>
          <v-col cols="6">
            <v-text-field
              outlined
              v-model="customer.cell_number"
              :rules="nameRules"
              label="Cell"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="6">
            <v-text-field
              outlined
              v-model="customer.district"
              :rules="nameRules"
              label="District"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="6">
            <v-text-field outlined v-model="customer.city" :rules="nameRules" label="City" required></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-text-field
              outlined
              v-model="customer.address"
              :rules="nameRules"
              label="Address"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="6">
            <v-text-field
              outlined
              v-model="customer.tax_office"
              :rules="nameRules"
              label="Tax Office"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="6">
            <v-text-field
              outlined
              v-model="customer.tax_no"
              :rules="nameRules"
              label="Tax No"
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
              v-if="customer.id !== 0"
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
      customer: {
        id: 0,
        name: "",
        address: "",
        city: "",
        tax_office: "",
        tax_no: "",
        cell_number: ""
      },
      nameRules: [v => !!v || "This field is required"],
      valid: true,
      state: false
    };
  },
  methods: {
    ...mapActions([
      "add_customer",
      "update_customer",
      "get_customer",
      "delete_customer"
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
            if (this.customer.id === 0) {
              this.add_customer(this.customer);
              this.$toast.success("Customer Created!");
            } else {
              console.log(this.customer);
              this.update_customer(this.customer);
              this.$toast.success("Customer Update!");
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
            this.delete_customer(this.customer.id);
            this.$router.push("/customers");
            this.$toast.success("Customer Deleted!");
          }
        }
      });
    }
  },
  computed: {
    ...mapGetters(["getCustomer"])
  },
  created() {
    const id = this.$route.params.id;
    if (id !== undefined)
      this.get_customer(id).then(() => (this.customer = this.getCustomer));
  }
};
</script>

<style>
</style>