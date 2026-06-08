
console.log("script.js 파일이 정상적으로 로드되었습니다.");

function verifyPassword(button, action) {
    const boardId = button.dataset.id;

    const passwordElement = document.getElementById('commonPassword');
    const userTyped = passwordElement.value;

    if (!userTyped) {
        alert("비밀번호를 입력해주세요.");
        return;
    }

    if (action === 'delete' && !confirm("정말 삭제하시겠습니까?")) {
        return;
    }

    fetch(`/verify/${boardId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password: userTyped })
    })
    .then(response => response.json())
    .then(data => {
        if (data.match) {

            if (action === 'update') {
                location.href = `/update/${boardId}`;
            } else if (action === 'delete') {
                const form = document.createElement('form');
                    form.method = 'POST';
                    form.action = `/delete/${boardId}`;
                    document.body.appendChild(form);
                    form.submit();
            }
        } else {
            alert("비밀번호가 일치하지 않습니다.");
        }
    })
    .catch(error => console.error("에러 발생:", error));
}



function saveComment(button) {
    const boardId = button.dataset.id;
    const comment =  document.getElementById('new-comment').value;
    const password = document.getElementById('new-comment-pw').value;

    if (!comment || !password) {
        alert("댓글과 비밀번호를 입력해주세요");
        return;
    }

    fetch(`/comment/${boardId}`, {
        method: "POST",
        headers: {"Content-Type" : "application/json"},
        body: JSON.stringify({comment, password})
    })
        .then(response => {
            if (response.ok) {
                alert("댓글이 등록되었습니다.");
                location.reload();
            } else {
                alert("댓글 등록에 실패했습니다.");
            }
        })
        .catch(error => console.error("에러 발생 : ", error));
}

// ===== 댓글 비밀번호 검증 (수정/삭제 전) =====
function verifyCommentPassword(button, action) {
    const commentId = button.dataset.id;
    const password = document.getElementById('comment-pw-' + commentId).value;

    if (!password) {
        alert("비밀번호를 입력해주세요.");
        return;
    }

    if (action === 'delete' && !confirm("정말 삭제하시겠습니까?")) {
        return;
    }

    fetch(`/comment/verify/${commentId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password })
    })
        .then(response => response.json())
        .then(data => {
            if (data.match) {
                if (action === 'update') {
                    // 수정 입력창 표시, 기존 텍스트 숨김
                    document.getElementById('comment-text-' +
                        commentId).style.display = 'none';
                    document.getElementById('comment-edit-' +
                        commentId).style.display = 'inline';
                    document.getElementById('confirm-edit-' +
                        commentId).style.display = 'inline';
                } else if (action === 'delete') {
                    deleteComment(commentId);
                }
            } else {
                alert("비밀번호가 일치하지 않습니다.");
            }
        })
        .catch(error => console.error("에러 발생:", error));
}

// ===== 댓글 수정 확정 =====
function submitCommentUpdate(button) {
    const commentId = button.dataset.id;
    const newComment = document.getElementById('comment-edit-' +
        commentId).value;

    if (!newComment) {
        alert("댓글 내용을 입력해주세요.");
        return;
    }

    fetch(`/comment/${commentId}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ comment: newComment })
    })
        .then(response => {
            if (response.ok) {
                alert("댓글이 수정되었습니다.");
                location.reload();
            } else {
                alert("댓글 수정에 실패했습니다.");
            }
        })
        .catch(error => console.error("에러 발생:", error));
}

// ===== 댓글 삭제 =====
function deleteComment(commentId) {
    fetch(`/comment/${commentId}`, {
        method: "DELETE"
    })
        .then(response => {
            if (response.ok) {
                alert("댓글이 삭제되었습니다.");
                location.reload();
            } else {
                alert("댓글 삭제에 실패했습니다.");
            }
        })
        .catch(error => console.error("에러 발생:", error));
}