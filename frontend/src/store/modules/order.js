import axios from "axios";
import baseUrl from "../config";

const state = {
    order: {
        order_items: []
    },
    orders: {
        data: [],
        pagination: {
          num_pages: 1,
          current_page: 1
        }
    }
};

const getters = {
    getOrder: state => state.order,
    getOrders: state => state.orders
};

const actions = {
    async get_order({ commit }, id) {
        const res = await axios.get(`${baseUrl}order/${id}/`);
        commit("SET_ORDER", res.data);
    },
    async get_orders({ commit }, page) {
        let url = `${baseUrl}order/`;
        if(page !== undefined)
        url += `?page=${page}`
        const res = await axios.get(url);
        commit("SET_ORDERS", res.data);
    },
    async add_order({ commit }, order) {
        const res = await axios.post(`${baseUrl}order/`, order);
        commit("SET_ORDER", res.data);
    },
    async update_order({ commit }, order) {
        const res = await axios.put(`${baseUrl}order/${order.id}/`, customer);
        commit("SET_ORDER", res.data);
    },
    async delete_order({ commit }, id) {
        const res = await axios.delete(`${baseUrl}order/${id}/`);
    }
};

const mutations = {
    SET_ORDERS: (state, orders) => state.orders = orders,
    SET_ORDER: (state, order) => state.order = order,

};

export default {
    state,
    getters,
    actions,
    mutations
};
