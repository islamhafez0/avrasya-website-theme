/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

class Testimonials extends Component {
  static template = "theme_avrasya.testimonials";

  setup() {
    this.state = useState({
      testimonials: [],
      loading: true,
      error: null,
    });
    this.rpc = useService("rpc");
    this.notification = useService("notification");

    onWillStart(async () => {
      await this.fetchData();
    });
  }

  async fetchData() {
    this.state.loading = true;
    this.state.error = null;
    try {
      const result = await this.rpc("/api/testimonials", {}, { silent: true });
      if (result && Array.isArray(result)) {
        this.state.testimonials = result;
      } else {
        throw new Error("Invalid response format from server");
      }
    } catch (error) {
      console.error("Failed to fetch testimonials:", error);
      this.state.error = "Failed to load testimonials. Please try again later.";
      this.notification.add(this.state.error, {
        type: "danger",
        sticky: false,
      });
    } finally {
      this.state.loading = false;
    }
  }

  retryFetch() {
    this.fetchData();
  }
}

registry
  .category("public_components")
  .add("theme_avrasya.testimonials", Testimonials);
