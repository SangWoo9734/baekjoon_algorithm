import sys
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.left = None
        self.right = None

def insert_node(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            insert_node(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            insert_node(parent.right, child)

def preorder_traversal(node, result):
    if node is not None:
        result.append(node.value)
        preorder_traversal(node.left, result)
        preorder_traversal(node.right, result)

def postorder_traversal(node, result):
    if node is not None:
        postorder_traversal(node.left, result)
        postorder_traversal(node.right, result)
        result.append(node.value)

def solution(nodeinfo):
    # 노드 번호를 추가하여 정렬하기 쉽게 변환
    nodes = [(i + 1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    # y 값을 기준으로 내림차순, x 값을 기준으로 오름차순 정렬
    nodes.sort(key=lambda x: (-x[2], x[1]))

    # 첫 번째 노드를 루트로 설정
    root = TreeNode(nodes[0][0], nodes[0][1], nodes[0][2])

    # 나머지 노드를 트리에 삽입
    for i in range(1, len(nodes)):
        insert_node(root, TreeNode(nodes[i][0], nodes[i][1], nodes[i][2]))

    # 전위 순회 및 후위 순회 결과
    preorder_result = []
    postorder_result = []

    preorder_traversal(root, preorder_result)
    postorder_traversal(root, postorder_result)

    return [preorder_result, postorder_result]
