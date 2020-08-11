<template>
  <v-card>
    <v-card-title>
      {{ title }}
      <v-spacer></v-spacer>
    </v-card-title>
    <v-divider class="mb-4"></v-divider>
    <v-data-table
      :headers="headers"
      :items="items"
      :search="search"
      hide-default-footer
      @click:row="rowClick"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-btn color="primary" dark class="mb-2" @click="newItem()" v-if="edit">
               <v-icon>mdi-plus</v-icon>
            New Item</v-btn>
          <v-spacer></v-spacer>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
      </template>
    </v-data-table>
    <v-pagination
      v-if="pagination"
      v-model="pagination.current_page"
      :length="pagination.num_pages"
      class="pb-5"
      @input="next"
    ></v-pagination>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      search: ""
    };
  },
  props: {
    headers: Array,
    edit: {
      type: Boolean,
      default: true
    },
    items: {},
    pagination: {
      num_pages: {
        type: Number,
        default: 1
      },
      current_page: {
        type: Number,
        default: 1
      }
    },
    title: String
  },
  methods: {
    newItem() {
      this.$emit("new_item");
    },
    editItem(item) {
      this.$emit("edit_item", item.id);
    },
    next(page) {
      this.$emit("change_page", page);
    },
    rowClick: function(item, row) {
      this.$emit("selected", item);
    }
  }
};
</script>