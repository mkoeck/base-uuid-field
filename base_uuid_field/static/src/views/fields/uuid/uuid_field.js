/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { Component, useRef, useState } from "@odoo/owl";
import { CopyClipboardCharField } from "@web/views/fields/copy_clipboard/copy_clipboard_field";

export class UUIDField extends CopyClipboardCharField {
    setup() {
        super.setup();
    }
    get type() {
        return "char";
    }
}

function extractProps({ attrs }) {
    return {
        string: attrs.string,
        disabledExpr: attrs.disabled,
    };
}

export const uuidField = {
    component: UUIDField,
    displayName: _t("UUID"),
    supportedTypes: ["uuid"],
    extractProps,
};

registry.category("fields").add("uuid", uuidField);