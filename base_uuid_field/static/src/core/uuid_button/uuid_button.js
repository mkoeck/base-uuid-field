import { browser } from "@web/core/browser/browser";
import { Tooltip } from "@web/core/tooltip/tooltip";
import { usePopover } from "@web/core/popover/popover_hook";
import { Component, useRef } from "@odoo/owl";

export class UUIDButton extends Component {
    static template = "base_uuid_field.UUIDButton"

    static props = {
        className: { type: String, optional: true },
        disabled: { type: Boolean, optional: true },
        successText: { type: String, optional: true },
        icon: { type: String, optional: true },
        onGenerate: { type: Function, optional: true},
        record: { type: Object, optional: true},
        name: { type: String, optional: true}
    };

    setup() {
        this.button = useRef("button");
        this.popover = usePopover(Tooltip);
    }

    showTooltip() {
        this.popover.open(this.button.el, { tooltip: this.props.successText });
        browser.setTimeout(this.popover.close, 800);
    }

    generateUUID() {
        return crypto.randomUUID();
    }

    async onClick() {
        this.props.onGenerate(this.generateUUID());

        this.showTooltip();
    }
}