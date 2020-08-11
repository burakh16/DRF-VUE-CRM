import axios from "axios";
import baseUrl from "../config";

const state = {
    product: {},
    products: {
        data: [],
        pagination: {
          num_pages: 1,
          current_page: 1
        }
    }
};

const getters = {
    getProduct: state => state.product,
    getProducts: state => state.products
};

const actions = {
    async get_product({ commit }, id) {
        const res = await axios.get(`${baseUrl}product/${id}/`);
        commit("SET_PRODUCT", res.data);
    },
    async get_products({ commit }, page) {
        let url = `${baseUrl}product/`;
        if(page !== undefined)
        url += `?page=${page}`
        const res = await axios.get(url);
        commit("SET_PRODUCTS", res.data);
    },
    async get_available_products({ commit },page) {
        let url = `${baseUrl}product/available/`;
        if(page !== undefined)
        url += `?page=${page}`
        const res = await axios.get(url);
        commit("SET_PRODUCTS", res.data);
    },
    async add_product({ commit }, product) {
        const res = await axios.post(`${baseUrl}product/`, product);
        commit("SET_PRODUCT", res.data);
    },
    async update_product({ commit }, product) {
        const res = await axios.put(`${baseUrl}product/${product.id}/`, product);
        commit("SET_PRODUCT", res.data);
    },
    async delete_product({ commit }, id) {
        const res = await axios.delete(`${baseUrl}product/${id}/`);
    }
};

const mutations = {
    SET_PRODUCTS: (state, products) => state.products = products,
    SET_PRODUCT: (state, product) => state.product = product,

};

export default {
    state,
    getters,
    actions,
    mutations
};
