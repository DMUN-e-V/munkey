const React = window.React;
const Modifier = window.DraftJS.Modifier;
const EditorState = window.DraftJS.EditorState;

// Not a real React component – just creates the entities as soon as it is rendered.
class MUNkeyLINKSource extends React.Component {
    render() {
        ModalWorkflow({
            url: "/admin/choose-munkey-link",
            onload: {
                'munkey_link': function (modal, jsonData) {
                    $('form', modal.body).on('submit', function () {
                        modal.postForm(this.action, $(this).serialize());
                        return false;
                    });
                },
                'munkey_link_chosen': function (modal, jsonData) {
                    modal.respond('linkChosen', jsonData['result']);
                    modal.close();
                },
            },
            responses: {
                linkChosen: (linkData) => {
                    const {editorState, entityType, onComplete} = this.props;

                    const content = editorState.getCurrentContent();
                    const selection = editorState.getSelection();

                    // Uses the Draft.js API to create a new entity with the right data.
                    const contentWithEntity = content.createEntity(entityType.type, 'IMMUTABLE', {
                        name: linkData.name,
                    });
                    const entityKey = contentWithEntity.getLastCreatedEntityKey();

                    const newContent = Modifier.replaceText(content, selection, linkData.title, null, entityKey);
                    const nextState = EditorState.push(editorState, newContent, 'insert-characters');

                    onComplete(nextState);
                }
            }
        });
        return null;
    }
}

window.draftail.registerPlugin({
    type: 'MUNkeyLINK',
    source: MUNkeyLINKSource,
});