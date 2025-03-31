/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { Component, useRef, useState } from "@odoo/owl";
import { CopyClipboardCharField } from "@web/views/fields/copy_clipboard/copy_clipboard_field";
import { CopyButton } from "@web/core/copy_button/copy_button";
import { UUIDButton } from "@base_uuid_field/core/uuid_button/uuid_button";
import { CharField } from "@web/views/fields/char/char_field";

export class UUIDField extends CopyClipboardCharField {
    static template = "base_uuid_field.UUIDField";
    static components = { Field: CharField, UUIDButton, CopyButton};
    
    setup() {
        super.setup();
    }

    get uuidSucessText() {
        return _t("Generated")
    }

    get uuidButtonClassName() {
        return this.copyButtonClassName()
    }

    get uuidButtonIcon() {
        return "fa-refresh";
    }

    async setUUID(uuid) {
        await this.record.update({[this.name]: uuid})
    }
}

export const uuidField = {
    component: UUIDField,
    displayName: _t("UUID"),
    supportedTypes: ["uuid"],
};

registry.category("fields").add("uuid", uuidField);